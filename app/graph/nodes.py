from app.agents.planner_agent import planner_agent
from app.agents.backend_agent import backend_agent
from app.agents.frontend_agent import frontend_agent
from app.graph.state import AgentState
from app.tools.directory_tool import create_directory
from app.tools.file_writer import write_file
from app.memory.memory_manager import memory_manager
from app.tools.file_reader import read_project
from app.agents.reviewer_agent import reviewer_agent
from app.config import settings

def planner_node(state: AgentState) -> AgentState:
    """
    Planner Node

    Takes the user requirement from the state,
    invokes the planner agent,
    and stores the generated project plan
    back into the state.
    """

    #search similar documents
    documents = memory_manager.search(
        query=state["requirement"],
        k=3
    )

    #convert this documents to string because llm can't understand documents
    memory = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    #we pass this memory as a context with user's requirment to the llm
    project_plan = planner_agent.invoke(
        requirement=state["requirement"],
        memory=memory
    )

    #we will save this response i.e project plan and plannar memory in which there will be requirement and project plan saved in the veotor store
    planner_memory = f"""
    requirement: {state["requirement"]}

    {project_plan.model_dump_json(indent=2)}
    """
    memory_manager.save(
        text=planner_memory,
        metadata={
            "agent": "planner"
        }
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

    #search similar documents
    documents = memory_manager.search(
        query=state["requirement"],
        k=3
    )

    #convert this documents to string
    memory = "\n\n".join(
        doc.page_content for doc in documents
    )

    #now we will pass this memory with project plan state to the backend agent
    backend_messages = backend_agent.invoke(
        requirement=state["project_plan"].model_dump_json(indent=2),
        memory=memory,
        output_path=state["GeneratedPath"]
    )

    #final Ai message
    final_response = backend_messages[-1]

    #now we have to save this backend_output with project_plan back to the vector stor
    backend_memory = f"""
    project_plan: {state['project_plan'].model_dump_json(indent=2)}

    Backend Result:
    {final_response.content}

    """
    memory_manager.save(
        text=backend_memory,
        metadata={
            "agent": "backend"
        }
    )

    return {
        "backend_code": backend_messages
    }

def frontend_node(state: AgentState) -> AgentState:
    """
    Frontend Node
    Takes the user requirement from the state,
    invokes the frontend agent,
    and stores the generated response
    back into the state.
    """

    documents = memory_manager.search(
        query=state["requirement"],
        k=3
    )

    memory = "\n\n".join(
        doc.page_content for doc in documents
    )

    frontend_messagges = frontend_agent.invoke(
        requirement=state["project_plan"].model_dump_json(indent=2),
        memory=memory,
        output_path=state["GeneratedPath"]
    )

    final_response = frontend_messagges[-1]

    frontend_memory = f"""
    requirement:

    {state["requirement"]}

    project_plan:

    {state["project_plan"].model_dump_json(indent=2)}

    frontend:

    {final_response.content}
    """

    memory_manager.save(
        text=frontend_memory,
        metadata={
            "agent":"frontend"
        }
    )

    return {
        "frontend_code": frontend_messagges
    }



def review_project_node(state: AgentState)-> AgentState:
    project_path = settings.PROJECT_ROOT
    project = read_project(project_path)

    documents = memory_manager.search(
        query = f"""
        {state["requirement"]}

        {state["project_plan"].model_dump_json()}
        """,
        k=3
    )

    memory = "\n\n".join(
        doc.page_content for doc in documents
    )

    reviewer_output = reviewer_agent.invoke(
        project=project,
        memory=memory
    )

    reviewer_memory = f"""
    requirement: 
    {state["requirement"]}
    frontend_code:
    {state["frontend_code"][-1].content}
    backend_code:
    {state["backend_code"][-1].content}
    reviewer:
    {reviewer_output.model_dump_json(indent=2)}
    """

    memory_manager.save(
        text=reviewer_memory,
        metadata={
            "agent": "reviewer"
        }
    )

    return{
        "review": reviewer_output
    }


