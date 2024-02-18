import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from pg_transform.pg_transform.assets import postgres_transform_dbt_assets
from pg_transform.pg_transform.constants import dbt_project_dir
from pg_transform.pg_transform.schedules import schedules
from elt_script.transfer_data import transfer_data_job

defs = Definitions(
    jobs=[transfer_data_job],
    assets=[postgres_transform_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
    },
)