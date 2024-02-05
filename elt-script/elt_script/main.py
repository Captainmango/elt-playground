import logging
import os
import sys
import time
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

    source_config = ConnectorConfig(
        user=os.environ["SOURCE_USER"],
        dbName=os.environ["SOURCE_DB"],
        password=os.environ["SOURCE_PASS"],
        host="source_db",
        port=os.environ["SOURCE_PORT"],
    )

    dest_config = ConnectorConfig(
        user=os.environ["DEST_USER"],
        dbName=os.environ["DEST_DB"],
        host="destination_db",
        password=os.environ["DEST_PASS"],
        port=os.environ["DEST_PORT"],
    )

    with PsqlConnector() as connector:
        connector.read(source_config)
        connector.write(dest_config)

    logger.info("Finished ELT process")
