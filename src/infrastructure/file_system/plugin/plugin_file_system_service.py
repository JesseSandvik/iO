import os

from enum import Enum

from src.infrastructure.file_system import FileSystemService

class PluginFileSystemSettings(Enum):
    PROJECT_ROOT_DIRECTORY_NAME='iO'
    DEFAULT_PLUGIN_CONFIGURATION_FILE_NAME = 'plugin.yaml'

class PluginFileSystemService(FileSystemService):

    @staticmethod
    def get_project_root_directory() -> str:
        current_directory = os.getcwd()
        return current_directory[0:current_directory.find(
            PluginFileSystemSettings.PROJECT_ROOT_DIRECTORY_NAME.value) + 
                len(PluginFileSystemSettings.PROJECT_ROOT_DIRECTORY_NAME.value)]
