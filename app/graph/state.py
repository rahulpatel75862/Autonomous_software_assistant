from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph.message import add_messages

from app.shemas.planner_schema import PlannerOutput

from app.shemas.frontend_schema import FrontendOutput

from app.shemas.backend_schema import BackendOutput


class AgentState(TypedDict):
    """
    Shared state for the complete LangGraph workflow.

    Every node receives this state,
    updates the required fields,
    and returns the updated state.
    """

    # User Requirement
    requirement: str

    # Conversation History
    messages: Annotated[list, add_messages]

    # Planner Output
    project_plan: PlannerOutput | None

    # Backend Agent Output
    backend_code: BackendOutput | None

    # Frontend Agent Output
    frontend_code: FrontendOutput | None

    # Database Agent Output
    database_schema: str | None

    # Testing Agent Output
    tests: str | None

    # Reviewer Agent Output
    review: str | None

    # Documentation Agent Output
    documentation: str | None

    generated_project_path: str | None