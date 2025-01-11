Local RAG Agent with Llama 3.2 Documentation
This documentation provides a comprehensive guide to setting up, running, and understanding the Local RAG Agent project, which implements a Retrieval-Augmented Generation (RAG) system using Llama 3.2 via Ollama and Qdrant as the vector database.

Table of Contents
1.Overview
2.Features
3.Prerequisites
4.Installation
5.Configuration
6.Running the Application
7.Project Structure
8.Dependencies
9.Troubleshooting
10.FAQs

1. Overview
The Local RAG Agent is a fully local implementation of a Retrieval-Augmented Generation (RAG) system. It uses Llama 3.2 as the language model through Ollama and Qdrant as the vector database for efficient vector search. The project includes an interactive playground interface for users to interact with the RAG agent.

2. Features
Fully Local RAG Implementation: No external API dependencies.
Powered by Llama 3.2: Utilizes the Ollama framework for local LLM inference.
Vector Search with Qdrant: Efficient vector search capabilities using the Qdrant vector database.
Interactive Playground Interface: A user-friendly interface to interact with the RAG agent.
PDF Knowledge Base: Supports loading and querying PDF documents for RAG.

3. Prerequisites
Before setting up the project, ensure the following are installed:
Python 3.8+
Docker (for running Qdrant)
Ollama (for running Llama 3.2 and OpenHermes)
Git (for cloning the repository)

4. Installation
Follow these steps to set up the project:
Step 1: Clone the Repository
Step 2: Install Dependencies
Install the required Python packages:
bash
Insert CodeRunCopy code
1pip install -r requirements.txt
Step 3: Set Up Qdrant
Pull and run the Qdrant vector database using Docker:
1docker pull qdrant/qdrant2docker run -p 6333:6333 qdrant/qdrant

Step 4: Install Ollama and Pull Models
Install Ollama and pull the required models:
1ollama pull llama3.2

5. Configuration
The project is configured through the app.py file. Key configurations include:
Vector Database Configuration
Collection Name: thai-recipe-index
Qdrant URL: http://localhost:6333/ or http://localhost:6333/dashboard
Embedder: OllamaEmbedder()
Knowledge Base Configuration
PDF URL: https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf
Vector Database: Qdrant
Agent Configuration
Agent Name: Local RAG Agent
Model: Ollama(id="llama3.2")
Knowledge Base: PDFUrlKnowledgeBase

6. Running the Application
To run the application, execute the following command:
1python app.py
Once the application is running, open your web browser and navigate to the URL provided in the console output to interact with the RAG agent through the playground interface.

7. Project Structure
The project consists of the following files:
app.py: Main application file containing the setup for the RAG agent, knowledge base, and vector database.
requirements.txt: Lists all Python dependencies required for the project.
README.md: Provides a quick start guide and overview of the project.

8. Dependencies
The project relies on the following Python packages:
phidata: Framework for building AI agents.
qdrant-client: Client for interacting with the Qdrant vector database.
ollama: Python client for Ollama.
pypdf: Library for working with PDF files.
openai: OpenAI API client (not used in this project but included).
fastapi: Web framework for serving the playground interface.
uvicorn: ASGI server for
