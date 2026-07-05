from langchain_core.prompts import ChatPromptTemplate


backend_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Generate a complete backend project.

            Rules:

            1. Return all required directories.

            2. Return every required file.

            3. Each file must contain complete production-ready code.

            4. Do not truncate code.

            5. Do not use placeholders.

            6. Return structured output only.
            """
        ),
        (
            "human",
            """
            Project Plan

            {project_plan}
            """
        )
    ]
)