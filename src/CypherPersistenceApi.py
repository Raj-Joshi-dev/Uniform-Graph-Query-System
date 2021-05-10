from persistence.neo4jImpl import Neo4jImpl
from persistence.memgraphImpl import MemgraphImpl
from utilities.Utilities import DatabaseType
from utilities.queryAnalyser import detectQueryType


class CypherPersistenceApi:
    def __init__(self, database_type):
        if database_type == DatabaseType.Neo4j:
            self.connection = Neo4jImpl()
        elif database_type == DatabaseType.Memgraph:
            self.connection = MemgraphImpl()

    def execute(self, query):
        # TODO add code to handle exceptions
        # TODO add code to handle create and delete queries if required
        queryType = detectQueryType(query)
        return self.connection.execute(query)

    def disconnect(self):
        self.connection.disconnect()
