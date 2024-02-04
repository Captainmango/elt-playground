from contextlib import AbstractContextManager
import logging
import sys
from types import TracebackType
from connector.connector_interface import DatabaseConnectorProtocol
from connector.configuration import ConnectorConfig


class UsqlConnector(DatabaseConnectorProtocol, AbstractContextManager):
    """
    The connector that can run all the commands needed to satisfy the ELT
    """
    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        
    def writeMySQL(self, config: ConnectorConfig):
        self.log.info(f"Writing to the MySQL database at {config.host}")
    
    def readPgSQL(self, config: ConnectorConfig):
        self.log.info(f"Reading from the Postgres database at {config.host}")
    
    def __exit__(self, __exc_type: type[BaseException] | None, __exc_value: BaseException | None, __traceback: TracebackType | None) -> bool | None:
        if __exc_type is not Exception:
            return True
        