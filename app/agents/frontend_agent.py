from app.prompts.frontend_prompts import frontend_prompt
from app.shemas.frontend_schema import FrontendOutput
from app.prompts.frontend_prompts import frontend_prompt
from app.llm.client import tool_llm
from app.tools.tool_executer import execute_tool_calls


class FrontendAgent:
    def __init__(self):
        self.llm = tool_llm

    def invoke(self, requirement: str, memory: str) -> FrontendOutput:
        messages = frontend_prompt.format_messages(
            project_plan = requirement,
            memory = memory
        )

        while True:
            ai_message = self.llm.invoke(
                messages
            )
            messages.append(ai_message)
            if not ai_message.tool_calls:
                break
            message = execute_tool_calls(messages)

        return message
    
frontend_agent = FrontendAgent()