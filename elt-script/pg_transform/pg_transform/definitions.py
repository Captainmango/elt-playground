import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from pg_transform.pg_transform.assets import postgres_transform_dbt_assets
from pg_transform.pg_transform.constants import dbt_project_dir
from pg_transform.pg_transform.schedules import schedules


defs = Definitions(
    assets=[postgres_transform_dbt_assets],
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir))
    },
)