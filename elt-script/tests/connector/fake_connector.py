from contextlib import AbstractContextManager
import logging
import sys
from types import TracebackType
from elt_script.connector.connector_interface import DatabaseConnectorProtocol
from elt_script.connector.configuration import ConnectorConfig


class FakeConnector(DatabaseConnectorProtocol, AbstractContextManager):
    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)
        self.log.addHandler(logging.StreamHandler(sys.stdout))
    
    def read(self, config: ConnectorConfig):
        # Create a fake SQL file using stringIO
        # Maybe check log writes too
        print("stuff")

    def write(self, config: ConnectorConfig):
        # Push the fake SQL file out. Probs easiest to check log writes for this
        print("more stuff")

    def __exit__(self, __exc_type: type[BaseException] | None, __exc_value: BaseException | None, __traceback: TracebackType | None) -> bool | None:
        if __exc_type is None:
            return True
        
        self.log.exception(__exc_value)
        raise __exc_type(__exc_value)