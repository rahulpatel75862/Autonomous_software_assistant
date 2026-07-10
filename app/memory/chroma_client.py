from app.memory.embeddings import embedding_model
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name = "autonomous_software_engineer",
    embedding_function = embedding_model,
    persist_directory = "./chroma_db"
)