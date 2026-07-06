from typing import List
from pydantic import BaseModel,Field


class GenerateDirectory(BaseModel):
    path: str=Field(
        description="Directory to be created."
    )

class GeneratedFile(BaseModel):
    path: str = Field(
        description="The path of file"
    )
    content: str = Field(
        description="Complete Source code."
    )

class FrontendOutput(BaseModel):
    directories: List[GenerateDirectory] = Field(
        description="Frontend Directories"
    )

    files: List[GeneratedFile] = Field(
        description="Frontend Files"
    )

    dependencies: List[str] = Field(
        description="Dependencies Used in the project"
    )