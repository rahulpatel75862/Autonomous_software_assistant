from pathlib import Path


class DirectoryTool:
    @staticmethod
    def create_directory(filepath: str):
        try:
            if not filepath:
                raise FileNotFoundError("File not found")
            path = Path(filepath)
            path.mkdir(parents=True, exist_ok=True)
            return f"{filepath} created succesfully"
        except Exception as e:
            raise RuntimeError(f"Error in Creating directory.")