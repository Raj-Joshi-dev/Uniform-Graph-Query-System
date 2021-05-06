import math
import utilities.memgraphConfig as mcfg
from persistence.connection import Connection
import mgclient


class MemgraphImpl(Connection):

    def __init__(self):
        self.connect(host=mcfg.host, port=mcfg.port)

    def connect(self, host, port):
        self.connection = mgclient.connect(host=host, port=port)
        print("connection successful")

    def execute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        return row
        # connection.commit()

    def disconnect(self):
        print("TODO not implemented.")
