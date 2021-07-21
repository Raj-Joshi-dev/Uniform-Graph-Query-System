import utilities.redisgraphConfig as rcfg
import redis
from redisgraph import Node, Edge, Graph, Path
from persistence.connection import Connection


class RedisImpl(Connection):

    def __init__(self):
        r = redis.Redis(host=rcfg.host, port=rcfg.port)
        self.redis_graph = Graph('DemoGraph', r)
        # self.connect(host=rcfg.host, port=rcfg.port)

    def connect(self):
        print("RedisGraph connection successful")

    def execute(self, index, query):
        result = self.redis_graph.query(query)
        raise Exception('Not implemented!')
        return {'result': [self.serialize_data(i, record) for i, record in enumerate(result)]}

    def serialize_data(self, index, row):
        raise Exception('Not implemented!')
        print(row)
        return dict(row)

    def disconnect(self):
        print("RedisGraph connection terminated")
