from contextlib import AbstractContextManager
from dataclasses import asdict
import logging
from subprocess import run
import os
from types import TracebackType
from connector.connector_interface import DatabaseConnectorProtocol
from connector.configuration import ConnectorConfig


class UsqlConnector(DatabaseConnectorProtocol, AbstractContextManager):
    """
    The connector that can run all the commands needed to satisfy the ELT
    """
    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)
        
    def writeMySQL(self, config: ConnectorConfig):
        self.log.info(f"Writing to the MySQL database at {config.host}")
        run(["usql", "--help"], env=asdict(config), check=True, shell=True)

        self.log.info(f"Write to MySQL database complete")
    
    def readPgSQL(self, config: ConnectorConfig):
        self.log.info(f"Reading from the Postgres database at {config.host}")
        
        run([
            f"usql postgres://{config.user}:{config.password}@{config.host}/{config.dbName}", 
            "-c 'select * from users;' > file.sql"
        ], env=asdict(config), check=True, shell=True)

        self.log.info(f"Read from the Postgres database complete")
    
    def __exit__(self, __exc_type: type[BaseException] | None, __exc_value: BaseException | None, __traceback: TracebackType | None) -> bool | None:
        if __exc_type is not Exception:
            return True
        