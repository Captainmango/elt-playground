from typing import Protocol


class DatabaseConnectorProtocol(Protocol):
    def read(self):
        pass

    def write(self):
        pass