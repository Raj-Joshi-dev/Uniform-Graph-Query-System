import csv
from pprint import pprint
import mgclient

# Make a connection to the database
connection = mgclient.connect(host='172.17.0.2', port=7687)

# Create a cursor for query execution
cursor = connection.cursor()

# Load the CSV file and create a node for each row
# with open('nodes.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for row in reader:
#         query = """CREATE (n:{label})
#                    SET n.title = '{title}'""".format(title=row[1], label=row[2])
#         cursor.execute(query)

# cursor.execute("""
#         CREATE (n:Person {name: 'Raj'})-[e:KNOWS]->
#                (m:Person {name: 'Joshi'})
#         RETURN n, e, m
#     """)

# A query to return all nodes
# query = "MATCH (e) RETURN e"

# A query to return all nodes with associated relationships
query = """MATCH(n)-[r]->(m)
        RETURN n, r, m
        """

# Execute the query
cursor.execute(query)

# Fetch one row of query results
row = cursor.fetchone()

# Print the first member in row
print(row[0])

# Make database changes persistent
connection.commit()
