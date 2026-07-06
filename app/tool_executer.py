from langchain_core.messages import AIMessage, ToolMessage
from app.tools.toolkit import Tools

tool_map = {}
for tool in Tools:
    tool_map[tool.name] = tool

def execute_tool_calls(messages: list):
    try:
        last_message = messages[-1]
        if not isinstance(last_message, AIMessage):
            return messages
        if not last_message.tool_calls:
            return messages
        for tool_call in last_message.tool_calls:
            tool = tool_map.get(tool_call["name"])
            
            if tool is None:
                continue

            result = tool.invoke(tool_call["args"])

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id = tool_call["id"]
                )
            )
            return messages
    except Exception as e:
        raise RuntimeError(f"something went wrong in execute tool calls function.")
