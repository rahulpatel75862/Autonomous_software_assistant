from app.prompts.backend_prompts import backend_prompt
from app.llm.client import model
from app.shemas.backend_schema import BackendOutput

class BackendAgent:
    def __init__(self):
        self.chain = backend_prompt | model.with_structured_output(BackendOutput)

    def invoke(self, requirement: str) -> BackendOutput:
        response = self.chain.invoke(
            {
                "project_plan": requirement
            }
        )
        return response

backend_agent = BackendAgent()