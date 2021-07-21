import pprint

from CypherPersistenceApi import CypherPersistenceApi
from utilities.Utilities import DatabaseType
from utilities.Utilities import exitCommands

flag = True


def printWelcomeMessage():
    print('This implementation only runs for one persistence mode at a time.')
    print('Enter one of the following options:')
    print('1. Neo4j')
    print('2. Memgraph')
    print('Enter "exit" to exit.')


def requestDatabaseType():
    dbType = DatabaseType.Unknown
    plainTextDatabaseType = input()
    if plainTextDatabaseType == "1":
        dbType = DatabaseType.Neo4j
    elif plainTextDatabaseType == "2":
        dbType = DatabaseType.Memgraph
    elif exitCommands.__contains__(plainTextDatabaseType):
        dbType = DatabaseType.Exit
    return dbType


def handleSloppyUsers():
    print("That was sloppy, please enter only a number, either 0 or 1.")
    printWelcomeMessage()
    return requestDatabaseType()


def requestQuery():
    print("Enter a query to be run, type \"exit\" to exit:")
    query = input()
    global flag
    if exitCommands.__contains__(query):
        flag = False
    if query == "":
        query = "MATCH (n:TBox) RETURN n"
    return query


def runQuery(query):
    # pprint.pprint(connection.execute(query))
    x = connection.execute(query)
    print(x)


printWelcomeMessage()
databaseType = requestDatabaseType()
while databaseType == DatabaseType.Unknown:
    databaseType = handleSloppyUsers()
if not databaseType == DatabaseType.Exit:
    connection = CypherPersistenceApi(databaseType)
    while flag:
        query = requestQuery()
        if not exitCommands.__contains__(query):
            runQuery(query)
    connection.disconnect()
print('The program will now exit.')
