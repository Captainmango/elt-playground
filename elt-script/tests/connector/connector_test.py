from tests.base_testcase import BaseScriptTestCase
from tests.connector.fake_connector import FakeConnector
from elt_script.connector.configuration import ConnectorConfig

class ConnectorTest(BaseScriptTestCase):

    def test_it_can_read_from_postgres(self):
        config = ConnectorConfig()
        with FakeConnector() as db:
            db.readPgSQL(config=config)
            

    def test_it_can_write_to_mysql(self):
        config = ConnectorConfig()
        self.conn.writeMySQL(config=config)