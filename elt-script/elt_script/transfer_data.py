import os
from elt_script.connector.configuration import ConnectorConfig
from elt_script.connector.connector_interface import DatabaseConnectorProtocol
from elt_script.connector.pg_connector import PsqlConnector

from dagster import AssetExecutionContext, Definitions, asset

def transfer_data(dbConn: DatabaseConnectorProtocol):
    source_config = ConnectorConfig(
        user=os.environ["SOURCE_USER"],
        dbName=os.environ["SOURCE_DB"],
        password=os.environ["SOURCE_PASS"],
        host="source_db",
        port=int(os.environ["SOURCE_PORT"]),
    )

    dest_config = ConnectorConfig(
        user=os.environ["DEST_USER"],
        dbName=os.environ["DEST_DB"],
        host="destination_db",
        password=os.environ["DEST_PASS"],
        port=int(os.environ["DEST_PORT"]),
    )

    connector: DatabaseConnectorProtocol
    with dbConn as connector:
        connector.read(source_config)
        connector.write(dest_config)

@asset(compute_kind="python")
def transfer_data_asset(context: AssetExecutionContext):
    context.log.info("Starting transfer to destination table")
    connector = PsqlConnector(context.log)
    transfer_data(connector)
    context.log.info("Finished moving data to destination table")


defs = Definitions(
    assets=[transfer_data_asset]
)