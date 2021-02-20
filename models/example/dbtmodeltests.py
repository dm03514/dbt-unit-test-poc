import unittest
from contextlib import contextmanager

from unittest.mock import patch

import pandas as pd
import dbt.main as dbt
from dbt.adapters.factory import get_adapter, reset_adapters, register_adapter
from dbt.config import RuntimeConfig
from dbt.context import providers


class TestArgs:
    def __init__(self, kwargs):
        self.which = 'run'
        self.single_threaded = False
        self.profiles_dir = None
        self.project_dir = None
        self.__dict__.update(kwargs)


class DBTModelTestCase(unittest.TestCase):
    conn_name = '__test'

    @contextmanager
    def get_connection(self, name=None):
        """Create a test connection context where all executed macros, etc will
        get self.adapter as the adapter.
        This allows tests to run normal adapter macros as if reset_adapters()
        were not called by handle_and_check (for asserts, etc)
        """
        if name is None:
            name = '__test'
        with patch.object(providers, 'get_adapter', return_value=self.adapter):
            with self.adapter.connection_named(name):
                conn = self.adapter.connections.get_thread_connection()
                yield conn

    def setUp(self):
        reset_adapters()

        kwargs = {
            'profile': 'ci',
            'profiles_dir': 'conf/',
            'target': None,
        }

        config = RuntimeConfig.from_args(TestArgs(kwargs))
        register_adapter(config)
        adapter = get_adapter(config)
        adapter.cleanup_connections()
        self.adapter = adapter

    def execute_model_with_results(self, model):
        dbt_args = [
            'run',
            '-m', model,
            '--profiles-dir', 'conf/',
            '--profile', 'ci'
        ]
        resp, success = dbt.handle_and_check(dbt_args)
        self.assertTrue(success)
        self.assertEqual(1, len(resp.results))
        rs = resp.results[0]
        print(rs.node.relation_name)

        sql = 'SELECT * FROM {}'.format(rs.node.relation_name)

        with self.get_connection(self.conn_name) as conn:
            df = pd.read_sql(sql, conn.handle)
            print(df)
            return df

    def assertDFEqual(self, df1, df2):
        self.assertTrue(
            df1.equals(df2), '\n{} \n not equal to:\n{}'.format(
                df1,
                df2
            )
        )
