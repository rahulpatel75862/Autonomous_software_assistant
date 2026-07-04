from langchain_openai import ChatOpenAI
from app.config import settings

model = ChatOpenAI(
    model=settings.MODEL_NAME,
    api_key=settings.API_KEY,
    base_url=settings.BASE_URL,
    temperature=settings.TEMPERATURE,
)