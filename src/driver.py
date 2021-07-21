import jsonlines

from CypherPersistenceApi import CypherPersistenceApi
from utilities.Utilities import DatabaseType
from utilities.Utilities import readQueriesFromFile
from utilities.executionTimer import ExecutionTimer


def run_query(index, query):
    # pprint.pprint(connection.execute(query))
    x = connection.execute(index, query)
    # print(x)
    return json_generator(x)
    # print(x)
    # return x


# older way
# def json_test(records):
#     with open("output/data.json", "a") as f:
#         json.dump(x, f, indent=2)

# with jsonlines.open('output/output.json', mode='a') as writer:
#     writer.write(x)
#     writer.close()


def json_generator(x):
    with jsonlines.open('output/output.json', mode='a') as writer:
        writer.write(x)
        writer.close()


queries = readQueriesFromFile("queries.txt")
if queries[0] == "1":
    databaseType = DatabaseType.Neo4j
elif queries[0] == "2":
    databaseType = DatabaseType.Memgraph
elif queries[0] == "3":
    databaseType = DatabaseType.RedisGraph
else:
    databaseType = DatabaseType.Unknown
    print("Invalid data store!")
connection = CypherPersistenceApi(databaseType)
queries = queries[1:]
executionTimer = ExecutionTimer()
executionTimer.start()
for index, query in enumerate(queries, start=1):
    for i in range(1):
        print("\n==\n")
        run_query(index, query)
executionTimer.stop()
connection.disconnect()
print('The program will now exit.')
