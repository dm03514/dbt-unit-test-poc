Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](http://slack.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


```
$ dbt run --profiles-dir=conf/ --profile=ci
Running with dbt=0.19.0
Found 2 models, 4 tests, 0 snapshots, 0 analyses, 138 macros, 0 operations, 0 seed files, 0 sources, 0 exposures

14:40:32 | Concurrency: 8 threads (target='ci')
14:40:32 |
14:40:32 | 1 of 2 START table model test.my_first_dbt_model..................... [RUN]
14:40:33 | 1 of 2 OK created table model test.my_first_dbt_model................ [SELECT 2 in 0.10s]
14:40:33 | 2 of 2 START view model test.my_second_dbt_model..................... [RUN]
14:40:33 | 2 of 2 OK created view model test.my_second_dbt_model................ [CREATE VIEW in 0.06s]
14:40:33 |
14:40:33 | Finished running 1 table model, 1 view model in 0.31s.

Completed successfully

Done. PASS=2 WARN=0 ERROR=0 SKIP=0 TOTAL=2
```

# Executing Model Tests


```
# install the dbt-model-tests into your path
$ git clone git@github.com:dm03514/dbt-model-tests.git
$ cd dbt-model-tests
$ python setup.py develop

# install dbt deps to pull in required macros
$ dbt deps

# Execute tests
$ python -m unittest models/example/test_my_first_dbt_model.py
$ DBT_MODEL_TEST_ENABLED=1 DBT_MODEL_TEST_IDENTIFIER_PREFIX="test1_" python -m unittest models/example/test_my_second_dbt_model.py
```
