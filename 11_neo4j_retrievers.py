import os
from dotenv import find_dotenv, load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.neo4j_vector import Neo4jVector

load_dotenv(find_dotenv(filename='.env'))
embedding_provider = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

movie_plot_vector = Neo4jVector.from_existing_index(
    embedding_provider,
    url=os.getenv("NEO4J_URL"),
    username=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD"),
    index_name="moviePlots",
    embedding_node_property="embedding",
    text_node_property="plot",
)
# result = movie_plot_vector.similarity_search("A movie where aliens land and attack earth.")
result = movie_plot_vector.similarity_search("A movie where aliens land and attack earth.", k=1)
for doc in result:
    print(doc.metadata["title"], "-", doc.page_content)