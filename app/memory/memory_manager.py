from langchain_core.documents import Document
from app.memory.chroma_client import vector_store


class MemoryManager:
    def __init__(self):
        self.vector_store = vector_store

    def save(self, text: str, metadata: dict)-> None:
        document = Document(
            page_content=text,
            metadata = metadata
        )
        self.vector_store.add_documents([document])

    def search(self, query, k: int = 5):
         """
         search similar documents from the vector store
         """

         return self.vector_store.similarity_search(query = query, k=k)
    
    def get_all(self):
            return self.vector_store.get()
    
        
    def delete_all(self):
        return self.vector_store.delete_collection()
    
memory_manager = MemoryManager()