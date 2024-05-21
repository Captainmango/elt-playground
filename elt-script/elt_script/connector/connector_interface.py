from logging import Logger
from typing import Protocol
from elt_script.connector.logging_contextmanager import LoggingContextManager
from elt_script.connector.connector_readwriter import ConnectorReadWriter


class DatabaseConnectorProtocol(ConnectorReadWriter, LoggingContextManager, Protocol):
    """
    An interface the database connector must conform to in order to satisfy the script
    """

    _log:Logger
