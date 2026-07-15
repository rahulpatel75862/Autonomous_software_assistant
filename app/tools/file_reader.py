from pathlib import Path

def read_project(project_path: str)-> str:
    """
    It will read the content of every files and convert it into text.
    """
    try:
        content = []
        if not project_path:
            raise ValueError("project path not found")
        project = Path(project_path)

        for file in project.rglob("*"):
            if not file.is_file():
                continue
            text = file.read_text(encoding="utf-8")
            content.append(
                f"""
                File: {file.relative_to(project)}
                ==============================================
                {text}
                """
            )

        return "\n".join(content)
    except Exception as e:
        raise RuntimeError(f"Error in read project: {e}")
    
