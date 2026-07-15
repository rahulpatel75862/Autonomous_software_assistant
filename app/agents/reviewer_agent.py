from app.prompts.reviewer_prompts import reviewer_prompt
from app.llm.client import model
from app.shemas.reviewer_schema import ReviewerOutput


class ReviewerAgent:
    def __init__(self):
        self.chain = reviewer_prompt | model.with_structured_output(ReviewerOutput)

    def invoke(self, project: str, memory: str)-> ReviewerOutput:
        return self.chain.invoke(
            {
                "project": project,
                "memory": memory
            }
        )
    
reviewer_agent = ReviewerAgent()