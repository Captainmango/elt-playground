from contextlib import redirect_stdout
import io
from unittest.mock import patch

from tests.base_testcase import BaseScriptTestCase
from main import main
from elt_script.connector.configuration import ConnectorConfig


class EltTest(BaseScriptTestCase):
    @patch("elt_script.connector.pg_connector.PsqlConnector", autospec=True)
    def test_it_runs(self, mock_connector):
        fake_stdout = io.StringIO()

        def read(cfg: ConnectorConfig) -> None:
            fake_stdout.write(f"read from {cfg.host}/{cfg.dbName} \n")

        def write(cfg: ConnectorConfig) -> None:
            fake_stdout.write(f"write to {cfg.host}/{cfg.dbName} \n")

        mock_connector.read = read
        mock_connector.write = write
        mock_connector.__enter__ = lambda self : self
        mock_connector.__exit__ = lambda self, exc, exc_val, tb: True

        with redirect_stdout(fake_stdout):
            main(mock_connector)

        assert "read" in fake_stdout.getvalue()
        assert "write" in fake_stdout.getvalue()
        