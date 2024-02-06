from typing import Protocol
from elt_script.connector.configuration import ConnectorConfig


class ConnectorReadWriter(Protocol):
    def read(self, config: ConnectorConfig):
        pass

    def write(self, config: ConnectorConfig):
        pass