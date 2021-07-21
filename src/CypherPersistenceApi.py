from persistence.neo4jImpl import Neo4jImpl
from persistence.memgraphImpl import MemgraphImpl
from persistence.redisgraphImpl import RedisImpl
from utilities.Utilities import DatabaseType
from utilities.queryAnalyser import detectQueryType


class CypherPersistenceApi:
    def __init__(self, database_type):
        if database_type == DatabaseType.Neo4j:
            self.connection = Neo4jImpl()
        elif database_type == DatabaseType.Memgraph:
            self.connection = MemgraphImpl()
        else:
            self.connection = RedisImpl()

    def execute(self, index, query):
        # TODO add code to handle exceptions if any
        # queryType = detectQueryType(query)
        return self.connection.execute(index, query)

    def disconnect(self):
        self.connection.disconnect()
