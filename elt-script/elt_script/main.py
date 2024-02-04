import os
from connector.configuration import ConnectorConfig
from connector.usql_connector import UsqlConnector


if __name__ == "__main__":
    pg_config = ConnectorConfig()
    mysql_config = ConnectorConfig()

    with UsqlConnector() as connector:
        connector.readPgSQL(pg_config)
        connector.writeMySQL(mysql_config)

    print("it did something...")