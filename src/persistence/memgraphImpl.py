import utilities.memgraphConfig as mcfg
from persistence.connection import Connection
import mgclient


class MemgraphImpl(Connection):

    def __init__(self):
        self.connect(host=mcfg.host, port=mcfg.port)

    def connect(self, host, port):
        self.connection = mgclient.connect(host=host, port=port)
        self.connection.autocommit = True
        print("Memgraph connection successful")

    def execute(self, index,  query):
        print('executing query: ', index)
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        self.connection.commit()
        return self.serialize_response(result)

    def serialize_response(self, result):
        return {'result': [self.serialize_data_custom(i, row) for i, row in enumerate(result)]}

    # def serialize_data(self, index, row):
    #     print(row)
    #     return dict(row)

    def serialize_data_custom(self, index, row):
        graphDataTypeList = []
        for graphDataType in row:
            if isinstance(graphDataType, str) or isinstance(graphDataType, int):
                graphDataTypeDict = graphDataType
            else:
                graphDataTypeDict = graphDataType.properties
            print(graphDataTypeDict)
            graphDataTypeList.append(graphDataTypeDict)
        return graphDataTypeList

    def disconnect(self):
        self.connection_class = mgclient.Connection.close(self.connection)
        print("Memgraph connection terminated")
