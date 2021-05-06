import pprint

from CypherPersistenceApi import CypherPersistenceApi
from utilities import utilities

query = "MATCH (n:TBox) RETURN n"
executeNeo4j = True
executeMemgraph = True

if executeNeo4j:
    api = CypherPersistenceApi(utilities.DatabaseType.Neo4j)
    print(api.execute(query))
    api.disconnect()

if executeMemgraph:
    api = CypherPersistenceApi(utilities.DatabaseType.Memgraph)
    print(api.execute(query))
    api.disconnect()
