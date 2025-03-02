from dataclasses import dataclass

from src.domain.plugin import PluginCore, PluginMetadata

@dataclass
class Plugin:
    __metadata: PluginMetadata
    __core: PluginCore

    def __init__(self, metadata: PluginMetadata, core: PluginCore):
        self.metadata = metadata
        self.core = core

    def get_metadata(self) -> PluginMetadata:
        return self.__metadata
    
    def get_core(self) -> PluginCore:
        return self.__core
