import neo4j

from utilities import neo4jConfig as ncfg
from persistence.connection import Connection
from neo4j import GraphDatabase


def generate_select_query_function(query):
    """
    This function takes a query as parameter and returns a list of records.

    Keyword arguments:
    query -- str
    lamda -- list
    """
    # def select_query(tx):
    #     arr = []
    #     for record in tx.run(query):
    #         arr.append(record)
    #     return arr
    # return select_query

    """One liner anonymous function for the above commented code"""
    return lambda tx: [record for record in tx.run(query)]


class Neo4jImpl(Connection):
    """A Neo4j implementation class with required methods to execute a query."""

    def __init__(self):
        self.connect(ncfg.url, ncfg.user, ncfg.password)

    """Driver connection
    API reference - https://neo4j.com/docs/api/python-driver/4.2/api.html#boltdriver
    """

    def connect(self, url, user, password):
        self.driver = GraphDatabase.driver(url, auth=(user, password))
        print("Neo4j connection successful")

    """Driver execution
    API reference - https://neo4j.com/docs/api/python-driver/4.2/api.html#session-construction
    """

    def execute(self, index, query):
        print('executing query: ', index)
        with self.driver.session() as session:
            result = session.write_transaction(generate_select_query_function(query))
        # print(result)
        # return result
        return self.serialize_response(result)

    """Custom formatting for response"""

    def serialize_response(self, result):
        return {'result': [self.serialize_data_custom(index, record) for index, record in enumerate(result)]}

    def serialize_data_custom(self, index, record):
        """
        A custom serializer.

        Keyword arguments:
        index -- optional
        record -- required

        Record class documentation - https://neo4j.com/docs/api/python-driver/4.2/api.html#record
        """
        print('record ', index, ':', record)  # console print statement
        # Create an empty dictionary
        graph_data_type_list = {}
        # Iterate over the list of records also enumerating it.
        for j, graph_data_type in enumerate(record):
            # Check if the record has string or integer literal.
            if isinstance(graph_data_type, str) or isinstance(graph_data_type, int):
                # Return the keys and values of this record as a dictionary and store it inside graph_data_type_dict.
                graph_data_type_dict = record.data(j)
            else:
                # If the record fails the above check then manually convert them into dictionary with __dict__
                graph_data_type_dict = graph_data_type.__dict__
                # Remove unnecessary _graph as we do not need it to serialize from the record.
                if '_graph' in graph_data_type_dict:
                    del graph_data_type_dict['_graph']
                # Add a _start_node key from the record.
                if '_start_node' in graph_data_type_dict:
                    graph_data_type_dict['_start_node'] = graph_data_type_dict['_start_node'].__dict__
                    # Add a _labels key of start node from the record.
                    if '_labels' in graph_data_type_dict['_start_node']:
                        frozen_label_set = graph_data_type.start_node['_labels']
                        graph_data_type_dict['_start_node']['_labels'] = [v for v in frozen_label_set]
                    # Remove unnecessary _graph as we do not need it to serialize from the record.
                    if '_graph' in graph_data_type_dict['_start_node']:
                        del graph_data_type_dict['_start_node']['_graph']
                # Add a _start_node key from the record.
                if '_end_node' in graph_data_type_dict:
                    graph_data_type_dict['_end_node'] = graph_data_type_dict['_end_node'].__dict__
                    # Add a _labels key of start node from the record.
                    if '_labels' in graph_data_type_dict['_end_node']:
                        frozen_label_set = graph_data_type.start_node['_labels']
                        graph_data_type_dict['_end_node']['_labels'] = [v for v in frozen_label_set]
                    # Remove unnecessary _graph as we do not need it to serialize from the record.
                    if '_graph' in graph_data_type_dict['_end_node']:
                        del graph_data_type_dict['_end_node']['_graph']
                # Add other labels for representation from frozenset()
                if '_labels' in graph_data_type_dict:
                    frozen_label_set = graph_data_type_dict['_labels']
                    graph_data_type_dict['_labels'] = [v for v in frozen_label_set]
                # print(graph_data_type_dict) # test statement
            graph_data_type_list.update(graph_data_type_dict)

        # print(index, ': ', graphDataTypeList)
        # return {
        #     # index: record,
        #     index: record.__dict__,
        # }
        return graph_data_type_list

    # def serialize_data2(self, index, record):
    #     keys = record.keys()
    #     dict = {}
    #     for key in keys:
    #         graphDataType = record.value(key)
    #         if isinstance(graphDataType, str) or isinstance(graphDataType, int):
    #             graphDataTypeDict = record.data(key)
    #         else:
    #             graphDataTypeDict = graphDataType.__dict__
    #             if '_graph' in graphDataTypeDict:
    #                 del graphDataTypeDict['_graph']
    #             if '_start_node' in graphDataTypeDict:
    #                 graphDataTypeDict['_start_node'] = graphDataTypeDict['_start_node'].__dict__
    #                 if '_labels' in graphDataTypeDict['_start_node']:
    #                     frozenLabelSet = graphDataType.start_node['_labels']
    #                     graphDataTypeDict['_start_node']['_labels'] = [v for v in frozenLabelSet]
    #                 if '_graph' in graphDataTypeDict['_start_node']:
    #                     del graphDataTypeDict['_start_node']['_graph']
    #             if '_end_node' in graphDataTypeDict:
    #                 graphDataTypeDict['_end_node'] = graphDataTypeDict['_end_node'].__dict__
    #                 if '_labels' in graphDataTypeDict['_end_node']:
    #                     frozenLabelSet = graphDataType.start_node['_labels']
    #                     graphDataTypeDict['_end_node']['_labels'] = [v for v in frozenLabelSet]
    #                 if '_graph' in graphDataTypeDict['_end_node']:
    #                     del graphDataTypeDict['_end_node']['_graph']
    #             if '_labels' in graphDataTypeDict:
    #                 frozenLabelSet = graphDataTypeDict['_labels']
    #                 graphDataTypeDict['_labels'] = [v for v in frozenLabelSet]
    #         print(graphDataTypeDict)
    #         dict[key] = graphDataTypeDict
    #     return dict

    """This is an another workaround using API helper methods but it lacks ID field which is very important. 
    
    The following function does not return ID but only the resulting node information. We have to explicitly ask for 
    ID(n) in plain cypher if we need IDs.
    
    API reference -- https://neo4j.com/docs/api/python-driver/4.2/api.html#neo4j.Record.data
    """

    def serialize_data_api_way(self, index, record):
        # test = record.data()
        return [record.data() for r in record]

    def disconnect(self):
        self.driver.close()
        print("Neo4j connection terminated")
