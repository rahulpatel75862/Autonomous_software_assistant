from app.agents.planner_agent import planner_agent
from app.agents.backend_agent import backend_agent
from app.graph.state import AgentState
from app.tools.directory_tool import DirectoryTool
from app.tools.file_writer import FileWriterTool


def planner_node(state: AgentState) -> AgentState:
    """
    Planner Node

    Takes the user requirement from the state,
    invokes the planner agent,
    and stores the generated project plan
    back into the state.
    """

    project_plan = planner_agent.invoke(
        requirement=state["requirement"]
    )

    return {
        "project_plan": project_plan
    }

def backend_node(state: AgentState) -> AgentState:
    """
    Backend Node

    Takes the user requirement from the state,
    invokes the backend agent,
    and stores the generated response
    back into the state.
    """
    backend_output = backend_agent.invoke(
        requirement=state["project_plan"]
    )

    return {
        "backend_code": backend_output
    }

def write_project_node(state: AgentState) -> AgentState:
    backend_output = state["backend_code"]

    #create Directories
    for directory in backend_output.directories:
        DirectoryTool.create_directory(directory.path)

    #create files
    for file in backend_output.files:
        FileWriterTool.write_file(
            filepath=file.path,
            content=file.content
        )