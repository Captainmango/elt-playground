from contextlib import AbstractContextManager
import logging
from types import TracebackType
from connector.connector_interface import DatabaseConnectorProtocol
from connector.configuration import ConnectorConfig


class UsqlConnector(DatabaseConnectorProtocol, AbstractContextManager):
    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        
    def writeMySQL(self, config: ConnectorConfig):
        self.log.info(f"Writing to the MySQL database at {config.host}")
        print("Write did a thing")
    
    def readPgSQL(self, config: ConnectorConfig):
        self.log.info(f"Reading from the Postgres database at {config.host}")
    
    def __exit__(self, __exc_type: type[BaseException] | None, __exc_value: BaseException | None, __traceback: TracebackType | None) -> bool | None:
        if __exc_type is None:
            return True
        
        self.log.exception(__exc_value)
        raise __exc_type(__exc_value)
        