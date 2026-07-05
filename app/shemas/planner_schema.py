from typing import List
from pydantic import BaseModel, Field


class TechStack(BaseModel):
    Frontend: str | None = Field(
        default=None,
        description="Frontend Framework or library"
    )

    Backend: str | None = Field(
        default=None,
        description="Backend Framework"
    )

    Database: str | None = Field(
        default=None,
        description="Database used in the project"
    )
    languages: str | None = Field(
        default=None,
        description="Languages used in the project"
    )

class PlannerOutput(BaseModel):
    project_name: str = Field(
        description="project name"
    )

    project_types: str = Field(
        description="Type of project"
    )
    
    description: str = Field(
        description="Short summary of the project"
    )

    tech_stack: TechStack

    Features: List[str] = Field(
        description="Important Features"
    )

    tasks: List[str] = Field(
        description="Tasks should be executed in this order"
    )

    dependencies: List[str] = Field(
        description="Important External Dependencies"
    )