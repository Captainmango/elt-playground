from typing import Protocol
from elt_script.connector.configuration import ConnectorConfig


class ConnectorReadWriter(Protocol):
    def read(self, config: ConnectorConfig) -> None:
        raise NotImplementedError

    def write(self, config: ConnectorConfig) -> None:
        raise NotImplementedError