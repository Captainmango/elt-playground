from connector_interface import DatabaseConnectorProtocol


class UsqlConnector(DatabaseConnectorProtocol):
    def write(self):
        return super().write()
    
    def read(self):
        return super().read()