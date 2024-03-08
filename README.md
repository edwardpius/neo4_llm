# Neo4j LLM

```bash
cd ~/neo4j_llm
python3 -m venv .venv &&. .venv/bin/activate

pip install python_dotenv
pip install langchain
pip install openai
pip install langchain-openai
pip install langchainhub
pip install youtube-search
pip install neo4j
```

These files are the same code base
07_tools.py <==> 14_neo4j_movie_trailer_agent.py
13_neo4j_retriever_chain.py <==> 15_neo4j_movie_plots_vector_retriever.py