from dataclasses import dataclass

@dataclass(frozen=True)
class ConnectorConfig:
    """
    A class for holding a database configuration used in the connector class
    """

    user: str = ""
    password: str = ""
    host: str = ""
    dbName: str = ""
    port: int = 1234