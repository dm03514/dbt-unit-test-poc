import pandas as pd

from dbtmodeltest.testcase import DBTModelTestCase


class MyFirstDBTModelTestCase(DBTModelTestCase):
    def test_only_returns_id_1(self):
        my_first_dbt_model = pd.DataFrame([
            (1,),
            (2,),
            (None,)
        ], columns=['id'])

        out_df = self.execute_model_with_refs(
            model='models/example/my_second_dbt_model.sql',
            my_first_dbt_model=my_first_dbt_model,
        )

        expected_df = pd.DataFrame([
            (1.0,),
        ], columns=['id'])

        self.assertDFEqual(expected_df, out_df)
