from app.agents.planner_agent import planner_agent
from app.agents.backend_agent import backend_agent
from app.agents.frontend_agent import frontend_agent
from app.graph.state import AgentState
from app.tools.directory_tool import create_directory
from app.tools.file_writer import write_file
from app.memory.memory_manager import memory_manager
from app.tools.file_reader import read_project
from app.agents.reviewer_agent import reviewer_agent

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
        memory=memory
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
        memory=memory
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

def write_project_node(state: AgentState) -> AgentState:
    backend_output = state["backend_code"]
    frontend_output = state["frontend_code"]

    #create Directories
    for directory in backend_output.directories:
        create_directory.invoke(
            {
                "filepath": directory.path
            }
        )

    #create files
    for file in backend_output.files:
        write_file.invoke(
            {
                "filepath": file.path,
                "content":file.content
            }
        )

    #for frontend

    #create Directories
    for directory in frontend_output.directories:
        create_directory.invoke(
            {
                "filepath": directory.path
            }
        )

    #create files
    for file in frontend_output.files:
        write_file.invoke(
            {
                "filepath": file.path,
                "content":file.content
            }
        )

    project_root = backend_output.directories[0].path

    return {
        "generated_project_path": project_root
    }

def review_project_node(state: AgentState)-> AgentState:
    project_path = state["generated_project_path"]
    if project_path is None:
        raise ValueError("Generated project path not found.")
    project = read_project(project_path)

    documents = memory_manager.search(
        query=state["requirement"],
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
    {state["frontend_code"].model_dump_json(indent=2)}
    backend_code:
    {state["backend_code"].model_dump_json(indent=2)}
    reviewer:
    {reviewer_output.model_dump_json(indent=2)}
    """

    memory_manager.save(
        text=reviewer_memory,
        metadata={
            "agent": "Reviewer"
        }
    )

    return{
        "review": reviewer_output
    }


