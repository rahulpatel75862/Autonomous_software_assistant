from app.llm.client import model

response= model.invoke("Hello, Tell me about Sachin Tendulkar in 2 lines")
print(response.text)