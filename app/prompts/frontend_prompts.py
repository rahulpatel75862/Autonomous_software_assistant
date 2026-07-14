from langchain_core.prompts import ChatPromptTemplate


frontend_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a Senior React Architect.

Your responsibility is ONLY the frontend.

Rules:

1. Generate React frontend only.
2. Do not generate backend code.
3. Return structured output.
4. Generate production-ready React code.
5. Generate complete file contents.
6. Do not use placeholders.
7. Keep folder structure clean.
8. Use functional components.
9. Use React Hooks.
10. Follow modern React best practices.
            """
        ),
        (
            "human",
            """
            Project Plan

            {project_plan}

            =========================

            previous similar projects
            {memory}
            """
        )
    ]
)