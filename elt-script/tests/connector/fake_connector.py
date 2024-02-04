from contextlib import AbstractContextManager
from types import TracebackType
from elt_script.connector.connector_interface import DatabaseConnectorProtocol
from elt_script.connector.configuration import ConnectorConfig


class FakeConnector(DatabaseConnectorProtocol, AbstractContextManager):
    def readPgSQL(self, config: ConnectorConfig):
        print("stuff")

    def writeMySQL(self, config: ConnectorConfig):
        print("more stuff")

    def __exit__(self, __exc_type: type[BaseException] | None, __exc_value: BaseException | None, __traceback: TracebackType | None) -> bool | None:
        if __exc_type is None:
            return True
        
        self.log.exception(__exc_value)
        raise __exc_type(__exc_value)