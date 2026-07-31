from fastapi import APIRouter
from app.shemas.api_schema import GenerateRequest
from app.graph.builder import graph

router = APIRouter()

@router.post("/generate")
async def generate_project(request: GenerateRequest):
    response = graph.invoke(
        {
            "requirement":request.requirement,
            "GeneratedPath": request.output_path
        }
    )

    return response