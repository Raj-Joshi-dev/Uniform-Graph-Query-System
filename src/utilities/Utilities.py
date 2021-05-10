from enum import Enum


class DatabaseType(Enum):
    Neo4j = 0
    Memgraph = 1
    Unknown = 2
    Exit = 3


class QueryType(Enum):
    SELECT_MATCH = 101
    CREATE_CREATE = 201
    CREATE_SET = 202
    CREATE_MERGE = 203
    DELETE_DELETE = 301
    DELETE_REMOVE = 302
    UNKNOWN = 1001


regexMap = {QueryType.SELECT_MATCH: '^MATCH.+RETURN.+$'}

exitCommands = ["exit", "EXIT", "e"]
