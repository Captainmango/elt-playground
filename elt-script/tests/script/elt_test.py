import io
import os
from unittest.mock import patch
from elt_script.connector.configuration import ConnectorConfig
from tests.base_testcase import BaseScriptTestCase
from elt_script.main import main


class EltTest(BaseScriptTestCase):
    @patch("elt_script.connector.pg_connector")
    def test_it_runs(self, mock_connector):
        f = io.StringIO()

        mock_connector.read = lambda cfg : f.write(f"read from {cfg.host}/{cfg.dbName}")
        mock_connector.write = lambda cfg : f.write(f"write to {cfg.host}/{cfg.dbName}")
        mock_connector.__enter__ = lambda self : self

        main(mock_connector)

        assert(f.getvalue is not None)
        