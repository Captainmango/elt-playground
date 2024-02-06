from contextlib import AbstractContextManager
import logging
import subprocess
from types import TracebackType
from elt_script.connector.connector_interface import DatabaseConnectorProtocol
from elt_script.connector.configuration import ConnectorConfig


class PsqlConnector(DatabaseConnectorProtocol, AbstractContextManager):
    """
    The connector that can run all the commands needed to satisfy the ELT
    """
    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)
        
    def write(self, config: ConnectorConfig):
        self.log.info(f"Writing to the Postgres database at {config.host}")
        cmd = f"psql -h {config.host} -U {config.user} -d {config.dbName} -a -f data_dump.sql"
        subprocess.run(cmd, env=dict(PGPASSWORD=config.password), check=True, shell=True)
        self.log.info(f"Write to Postgres database complete")

    def read(self, config: ConnectorConfig):
        self.log.info(f"Reading from the Postgres database at {config.host}")
        cmd = f"pg_dump -h {config.host} -U {config.user} -d {config.dbName} -f data_dump.sql -w"
        subprocess.run(cmd, env=dict(PGPASSWORD=config.password), check=True, shell=True)
        self.log.info(f"Read from the Postgres database complete")

    def __exit__(self, __exc_type: type[BaseException] | None, __exc_value: BaseException | None, __traceback: TracebackType | None) -> bool | None:
        if __exc_type is not Exception:
            return True

        self.log.error(__exc_value)
        