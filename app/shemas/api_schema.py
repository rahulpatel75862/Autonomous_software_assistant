from pydantic import BaseModel

class GenerateRequest(BaseModel):
    requirement: str
    output_path: str