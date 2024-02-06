from logging import Logger
from types import TracebackType
from typing import Protocol, Self
from elt_script.connector.configuration import ConnectorConfig


class DatabaseConnectorProtocol(Protocol):
    """
    An interface the database connector must conform to in order to satisfy the script
    """
    _log: Logger

    def read(self, config: ConnectorConfig):
        pass

    def write(self, config: ConnectorConfig):
        pass

    def __enter__(self) -> Self:
        return self

    def __exit__(self, __exc_type: type[BaseException] | None, __exc_value: BaseException | None, __traceback: TracebackType | None) -> bool | None:
        if __exc_type is not Exception:
            return True

        self.log.error(__exc_value)
        return True

