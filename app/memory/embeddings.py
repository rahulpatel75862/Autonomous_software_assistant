from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import settings

embedding_model = GoogleGenerativeAIEmbeddings(
    model = "gemini-embedding-001",
    google_api_key = settings.API_KEY
)