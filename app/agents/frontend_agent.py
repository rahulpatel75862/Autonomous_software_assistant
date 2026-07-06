from app.prompts.frontend_prompts import frontend_prompt
from app.shemas.frontend_schema import FrontendOutput
from app.llm.client import model


class FrontendAgent:
    def __init__(self):
        self.chain = frontend_prompt | model.with_structured_output(FrontendOutput)

    def invoke(self, requirement: str) -> FrontendOutput:
        response = self.chain.invoke(
            {
                "project_plan": requirement
            }
        )
        return response
    
frontend_agent = FrontendAgent()