import math
from utilities import neo4jConfig as ncfg
from persistence.connection import Connection
from neo4j import GraphDatabase


class Neo4jImpl(Connection):

    def __init__(self):
        self.connect(ncfg.url, ncfg.user, ncfg.password)

    def connect(self, url, user, password):
        self.driver = GraphDatabase.driver(url, auth=(user, password))
        print("connection successful")

    def execute(self, query):
        with self.driver.session() as session:
            result = session.read_transaction(self.generate_select_query_function(query))
        return result

    def generate_select_query_function(self, query):
        def select_query(tx):
            arr = []
            for record in tx.run(query):
                arr.append(record)
            return arr

        return select_query

    def disconnect(self):
        self.driver.close()
        print("connection terminated")
