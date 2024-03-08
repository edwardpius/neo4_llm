import os
from dotenv import find_dotenv, load_dotenv
from langchain_community.graphs import Neo4jGraph

load_dotenv(find_dotenv(filename='.env'))
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URL"),
    username=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD")
)

result = graph.query("""
MATCH (m:Movie{title: 'Toy Story'}) 
RETURN m.title, m.plot, m.poster
""")

print(result)

print("\n")

print(graph.schema)