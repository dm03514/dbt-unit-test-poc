import pandas as pd

from .dbtmodeltests import DBTModelTestCase


class MyFirstDBTModelTestCase(DBTModelTestCase):

    def test_output_rows(self):
        df = pd.DataFrame([
            (1,),
            (None,)
        ], columns=['id'])

        out_df = self.execute_model_with_results(
            model='models/example/my_first_dbt_model.sql',
        )

        self.assertDFEqual(df, out_df)
