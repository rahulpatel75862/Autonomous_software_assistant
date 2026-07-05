from langgraph.graph import END, START, StateGraph

from app.graph.nodes import planner_node
from app.graph.state import AgentState

from app.graph.nodes import backend_node


graph_builder = StateGraph(AgentState)

graph_builder.add_node(
    "planner",
    planner_node
)

graph_builder.add_node(
    "backend",
    backend_node
)

graph_builder.add_edge(
    START,
    "planner"
)

graph_builder.add_edge(
    "planner",
    "backend",
)

graph_builder.add_edge(
    "backend",
    END
)

graph = graph_builder.compile()