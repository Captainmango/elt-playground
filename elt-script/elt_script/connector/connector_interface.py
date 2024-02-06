from logging import Logger
from elt_script.connector.logging_contextmanager import LoggingContextManager
from elt_script.connector.connector_readwriter import ConnectorReadWriter


class DatabaseConnectorProtocol(ConnectorReadWriter, LoggingContextManager):
    """
    An interface the database connector must conform to in order to satisfy the script
    """

    _log:Logger
