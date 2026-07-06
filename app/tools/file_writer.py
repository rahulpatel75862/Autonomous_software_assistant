from pathlib import Path
from langchain_core.tools import tool


@tool
def write_file(filepath: str, content: str):
    """
    Tool responsible for creating files and write the provided content in it.

    If the parent directory does not exist,
    it is created automatically.
    """
    try:
        if not filepath:
            raise FileNotFoundError("File not exists")
        elif not content:
            raise ValueError("Content not exists")

        path = Path(filepath)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            content,
            encoding="utf-8"
        )

        return f"{filepath} created successfully."

    except Exception as e:
        raise RuntimeError(f"Error in write file: {e}")