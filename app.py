# Import necessary libraries
from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.qdrant import Qdrant
from phi.embedder.ollama import OllamaEmbedder
from phi.playground import Playground, serve_playground_app

# Define the collection name for the vector database
collection_name = "thai-recipe-index"

# Set up Qdrant as the vector database with the embedder
vector_db = Qdrant(
    collection=collection_name,
    url="http://localhost:6333/",
    embedder=OllamaEmbedder(),
    timeout=30  # Increase timeout to 30 seconds
)

# from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
# from phi.vectordb.pgvector import PgVector

# pdf_knowledge_base = PDFKnowledgeBase(
#     path="data/pdfs",
#     # Table name: ai.pdf_documents
#     vector_db=vector_db,
#     reader=PDFReader(chunk=True),
# )

# Define the knowledge base with the specified PDF URL
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

# from phi.knowledge.csv import CSVKnowledgeBase
# from phi.vectordb.pgvector import PgVector

# knowledge_base = CSVKnowledgeBase(
#     path="data/csv",
#     # Table name: ai.csv_documents
#     vector_db=vector_db,
# )

# Load the knowledge base, comment out after the first run to avoid reloading
# knowledge_base.load(recreate=True, upsert=True)

# Create the Agent using Ollama's llama3.2 model and the knowledge base
agent = Agent(
    name="Local RAG Agent",
    model=Ollama(id="llama3.2"),
    knowledge=knowledge_base,
)

# UI for RAG agent
app = Playground(agents=[agent]).get_app()

# Run the Playground app
if __name__ == "__main__":
    serve_playground_app("app:app", reload=True)