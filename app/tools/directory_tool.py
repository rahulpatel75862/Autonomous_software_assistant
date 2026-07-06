from pathlib import Path
from langchain_core.tools import tool


@tool
def create_directory(filepath: str):
        """
        Tools responsible for creating directory
        """
        try:
            if not filepath:
                raise FileNotFoundError("File not found")
            path = Path(filepath)
            path.mkdir(parents=True, exist_ok=True)
            return f"{filepath} created succesfully"
        except Exception as e:
            raise RuntimeError(f"Error in Creating directory.")