from typing import Protocol
from connector.configuration import ConnectorConfig


class DatabaseConnectorProtocol(Protocol):
    def readPgSQL(self, config: ConnectorConfig):
        pass

    def writeMySQL(self, config: ConnectorConfig):
        pass