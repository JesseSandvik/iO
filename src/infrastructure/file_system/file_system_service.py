import yaml

from typing import Any

class FileSystemService:

    @staticmethod
    def get_yaml_file_contents(yaml_file_path: str) -> Any:
        with open(yaml_file_path) as file:
            file_content = yaml.safe_load(file)
        return file_content
