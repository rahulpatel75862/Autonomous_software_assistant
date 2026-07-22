from app.prompts.backend_prompts import backend_prompt
from app.llm.client import tool_llm
from langchain.messages import AIMessage
from app.tools.tool_executer import execute_tool_calls

class BackendAgent:
    def __init__(self):

        self.llm = tool_llm

        

    def invoke(self, requirement: str, memory: str) -> AIMessage:
        messages = backend_prompt.format_messages(
            project_plan = requirement,
            memory = memory
        )

        while True:
            ai_message = self.llm.invoke(messages)
            messages.append(ai_message)

            if not ai_message.tool_calls:
                break
            message = execute_tool_calls(messages)
        return message

backend_agent = BackendAgent()