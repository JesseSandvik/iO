import os

from typing import List

from src.domain.plugin import PluginMetadataLoader
from src.infrastructure.file_system.plugin.plugin_file_system_service import PluginFileSystemSettings, PluginFileSystemService

class FileSystemPluginMetadataLoader(PluginMetadataLoader):

    def __discover_plugins(self) -> List[str]:
        plugin_directory = os.path.join(PluginFileSystemService.get_project_root_directory(), 'plugins')
        found_plugins = []

        for root, dirs, files in os.walk(plugin_directory):
            for file in files:
                if file == PluginFileSystemSettings.DEFAULT_PLUGIN_CONFIGURATION_FILE_NAME.value:
                    found_plugins.append(os.path.join(root, file))
        return found_plugins

    def load(self):
        discovered_plugins = self.__discover_plugins()

        for plugin in discovered_plugins:
            print(f'> {plugin}')
