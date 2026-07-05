from pydantic import BaseModel, Field
from typing import List

class BackendOutput(BaseModel):
    folder_structure: List[str] = Field(
        description="Backend Folder structure of the project"
    )

    api_routes: List[str] = Field(
        description="Api routes of the project"
    )

    authentication: str

    orm: str

    dependencies: List[str]

    Db_connection: str


