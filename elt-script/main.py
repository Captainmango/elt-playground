import logging
import sys
from elt_script.connector.connector_interface import DatabaseConnectorProtocol
from elt_script.connector.pg_connector import PsqlConnector
from elt_script.transfer_data import transfer_data


def setup_logging() -> logging.Logger:
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    return root

def main(dbConn: DatabaseConnectorProtocol):
    logger = setup_logging()

    logger.info("Starting ELT Process")
    transfer_data(dbConn)

    logger.info("Finished ELT process")

if __name__ == "__main__":
    main(PsqlConnector())

