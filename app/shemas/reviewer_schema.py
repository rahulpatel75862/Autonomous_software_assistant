from typing import List
from pydantic import BaseModel, Field

class ReviewItem(BaseModel):
    category: str = Field(
        description="category of the review"
    )

    severity: str = Field(
        description="Severity of the review"
    )

    description: str = Field(
        description="Description of the issue"
    )

    suggestion: str = Field(
        description="Suggestion by llm to improvement if any"
    )

class ReviewerOutput(BaseModel):
    score: int = Field(
        description="Score given by llm after reviewing"
    )
    summary: str = Field(
        description="Summary of the Review"
    )
    issues: List[ReviewItem]