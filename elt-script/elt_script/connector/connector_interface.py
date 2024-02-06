from typing import Protocol
from elt_script.connector.configuration import ConnectorConfig


class DatabaseConnectorProtocol(Protocol):
    """
    An interface the database connector must conform to in order to satisfy the script
    """
    def read(self, config: ConnectorConfig):
        pass

    def write(self, config: ConnectorConfig):
        pass

