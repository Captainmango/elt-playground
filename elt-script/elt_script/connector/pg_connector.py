import logging
import subprocess

from elt_script.connector.connector_interface import DatabaseConnectorProtocol
from elt_script.connector.configuration import ConnectorConfig


class PsqlConnector(DatabaseConnectorProtocol):
    """
    The connector that can run all the commands needed to satisfy the ELT
    """

    def __init__(self, logger: logging.Logger) -> None:
        self._log = logger
        self._log.setLevel(logging.DEBUG)
        
    def write(self, config: ConnectorConfig):
        self._log.info(f"Writing to the Postgres database at {config.host}")
        cmd = f"psql -h {config.host} -U {config.user} -d {config.dbName} -a -f data_dump.sql"
        subprocess.run(cmd, env=dict(PGPASSWORD=config.password), check=True, shell=True)
        self._log.info("Write to Postgres database complete")

    def read(self, config: ConnectorConfig):
        self._log.info(f"Reading from the Postgres database at {config.host}")
        cmd = f"pg_dump -h {config.host} -U {config.user} -d {config.dbName} -f data_dump.sql -w"
        subprocess.run(cmd, env=dict(PGPASSWORD=config.password), check=True, shell=True)
        self._log.info("Read from the Postgres database complete")

        