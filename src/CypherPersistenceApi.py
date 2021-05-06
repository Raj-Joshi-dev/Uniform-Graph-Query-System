from persistence.neo4jImpl import Neo4jImpl
from persistence.memgraphImpl import MemgraphImpl
from utilities import utilities


class CypherPersistenceApi:
    def __init__(self, database_type):
        if database_type == utilities.DatabaseType.Neo4j:
            self.connection = Neo4jImpl()
        elif database_type == utilities.DatabaseType.Memgraph:
            self.connection = MemgraphImpl()

    def execute(self, query):
        return self.connection.execute(query)

    def disconnect(self):
        self.connection.disconnect()
