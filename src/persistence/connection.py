# Abstract class
from abc import ABC, abstractmethod


class Connection(ABC):

    @abstractmethod
    def execute(self, query):
        pass

# Create a config file for templates for Neo4j and Memgraph.
