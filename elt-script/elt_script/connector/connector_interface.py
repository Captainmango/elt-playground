from typing import Protocol
from connector.configuration import ConnectorConfig


class DatabaseConnectorProtocol(Protocol):
    """
    An interface the database connector must conform to in order to satisfy the script
    """
    def readPgSQL(self, config: ConnectorConfig):
        pass

    def writeMySQL(self, config: ConnectorConfig):
        pass