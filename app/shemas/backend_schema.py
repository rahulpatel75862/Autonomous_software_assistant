from typing import List
from pydantic import BaseModel,Field

class GeneratedDirectory(BaseModel):
    path: str = Field(
        description="The path of the dirctory"
    )
    

class GeneratedFile(BaseModel):
    path: str = Field(
        description="Relative file path"
    )

    content: str = Field(
        description="The content of the file"
    )

class BackendOutput(BaseModel):
    directories: List[GeneratedDirectory] = Field(
        description="Directories required for the backend"
    )

    files: List[GeneratedFile] = Field(
        description="Files required for the backend."
    )

    dependencies: List[str] = Field(
        description="dependencies of the project"
    )