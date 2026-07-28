from langchain_core.prompts import ChatPromptTemplate

reviewer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a Senior Software Engineer responsible for reviewing AI-generated software projects.

            Review the project thoroughly.

            Rules:

            1. Folder structure
            2. Code quality
            3. Architecture
            4. Best practices
            5. Scalability
            6. Error handling
            7. Security
            8. Naming conventions
            9. Production readiness

            Return ONLY structured output.

            Do not rewrite code.
            Do not generate code.
            Do not explain unnecessarily.
            """
        ),
        (
            "human",
            """

            previous similar reviews
            {memory}


            project_files

            {project}
            """
        )
    ]
)