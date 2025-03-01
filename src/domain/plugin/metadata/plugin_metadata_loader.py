from abc import ABC, abstractmethod
from typing import Dict

from .plugin_metadata import PluginMetadata

class PluginMetadataLoader(ABC):
    __plugin_metadata = Dict[str, PluginMetadata]

    def __init__(self):
        self.__plugin_metadata = {}
    
    def _add_plugin_metadata(self, plugin_metadata: PluginMetadata):
        self.__plugin_metadata[plugin_metadata.plugin_id] = plugin_metadata

    def get_plugin_metadata_by_id(self, id: str) -> PluginMetadata:
        return self.__plugin_metadata[id]
    
    def get_all_plugin_metadata(self) -> Dict[str, PluginMetadata]:
        return self.__plugin_metadata

    @abstractmethod
    def load(self):
        pass
