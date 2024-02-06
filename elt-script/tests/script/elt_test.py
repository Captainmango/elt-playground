from contextlib import redirect_stdout
import io
from unittest.mock import patch

from tests.base_testcase import BaseScriptTestCase
from main import main
from elt_script.connector.configuration import ConnectorConfig


class EltTest(BaseScriptTestCase):
    @patch("elt_script.connector.pg_connector")
    def test_it_runs(self, mock_connector):
        f = io.StringIO()

        def read(cfg: ConnectorConfig) -> None:
            f.write(f"read from {cfg.host}/{cfg.dbName} \n")

        def write(cfg: ConnectorConfig) -> None:
            f.write(f"write to {cfg.host}/{cfg.dbName} \n")

        mock_connector.read = read
        mock_connector.write = write
        mock_connector.__enter__ = lambda self : self

        with redirect_stdout(f):
            main(mock_connector)

        assert "read" in f.getvalue()
        assert "write" in f.getvalue()
        