import logging
import os
import sys
from connector.configuration import ConnectorConfig
from connector.pg_connector import PsqlConnector


def setup_logging() -> logging.Logger:
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    return root


if __name__ == "__main__":
    logger = setup_logging()

    logger.info("Starting ELT Process")

    pg_config = ConnectorConfig(
        user=os.environ["SOURCE_USER"],
        dbName=os.environ["SOURCE_DB"],
        password=os.environ["SOURCE_PASS"],
        host="source_db",
        port=os.environ["SOURCE_PORT"],
    )

    mysql_config = ConnectorConfig(
        user=os.environ["DEST_USER"],
        dbName=os.environ["DEST_DB"],
        host="destination_db",
        port=os.environ["DEST_PORT"],
    )

    with PsqlConnector() as connector:
        connector.read(pg_config)
        connector.write(mysql_config)

    logger.info("Finished ELT process")
