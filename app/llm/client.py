from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import settings
from app.tools.toolkit import Tools

model = ChatGoogleGenerativeAI(
    model=settings.MODEL_NAME,
    api_key=settings.API_KEY,
    temperature=settings.TEMPERATURE,
)

tool_llm = model.bind_tools(Tools)