from app.prompts.backend_prompts import backend_prompt
from app.llm.client import tool_llm
from langchain_core.messages import AIMessage
from app.tools.tool_executer import execute_tool_calls


class BackendAgent:
    def __init__(self):
        self.llm = tool_llm

    def invoke(
        self,
        requirement: str,
        memory: str,
        output_path: str
    ):
        messages = backend_prompt.format_messages(
            project_plan=requirement,
            memory=memory,
            output_path=output_path
        )

        while True:
            for m in messages:
                print("=" * 80)
                print(m.type)
                print(m.content)
            ai_message = self.llm.invoke(messages)
            messages.append(ai_message)

            # No more tool calls → finished
            if not ai_message.tool_calls:
                break

            # Execute all tool calls
            messages = execute_tool_calls(messages)

        return messages


backend_agent = BackendAgent()