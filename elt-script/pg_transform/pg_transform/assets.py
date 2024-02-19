import os
from dagster import AssetExecutionContext, AssetKey, Definitions, SourceAsset
from dagster_dbt import DbtCliResource, dbt_assets

from pg_transform.pg_transform.constants import dbt_manifest_path, dbt_project_dir

transfer_data_asset = SourceAsset(key=AssetKey(["elt-code", "default", "transfer_data_asset"]))

@dbt_assets(manifest=dbt_manifest_path)
def postgres_transform_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()


defs = Definitions(
    assets=[transfer_data_asset, postgres_transform_dbt_assets],
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir))
    },
)