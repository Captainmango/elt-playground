from tests.base_testcase import BaseScriptTestCase
from unittest.mock import patch, MagicMock
from elt_script.connector.configuration import ConnectorConfig
from elt_script.connector.pg_connector import PsqlConnector

class PsqlConnectorTest(BaseScriptTestCase):
    @patch('subprocess.run') 
    def test_write(self, mock_run):
        connector = PsqlConnector()
        
        config = ConnectorConfig(host='localhost', user='user', dbName='test_db', password='password')

        connector.write(config)

        mock_run.assert_called_with(
            f"psql -h {config.host} -U {config.user} -d {config.dbName} -a -f data_dump.sql",
            env=dict(PGPASSWORD=config.password),
            check=True,
            shell=True
        )

    @patch('subprocess.run')
    def test_read(self, mock_run):
        connector = PsqlConnector()
        config = ConnectorConfig(host='localhost', user='user', dbName='test_db', password='password')

        connector.read(config)

        mock_run.assert_called_with(
            f"pg_dump -h {config.host} -U {config.user} -d {config.dbName} -f data_dump.sql -w",
            env=dict(PGPASSWORD=config.password),
            check=True,
            shell=True
        )