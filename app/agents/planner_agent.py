from app.prompts.planner_prompts import planner_prompts
from app.llm.client import model
from app.shemas.planner_schema import PlannerOutput


class PlannerAgent:

    def __init__(self):

        self.chain = (
            planner_prompts
            | model.with_structured_output(PlannerOutput)
        )

    def invoke(self, requirement: str) -> PlannerOutput:

        return self.chain.invoke(
            {
                "requirements": requirement
            }
        )
    
planner_agent = PlannerAgent()