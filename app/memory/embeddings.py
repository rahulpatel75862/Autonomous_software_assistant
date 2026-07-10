from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import settings

embedding_model = GoogleGenerativeAIEmbeddings(
    model = "models/text-embedding-004",
    google_api_key = settings.API_KEY
)