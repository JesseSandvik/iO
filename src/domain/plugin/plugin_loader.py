from abc import ABC, abstractmethod
from typing import Dict

from src.domain.plugin import Plugin

class PluginLoader(ABC):
    __plugins = Dict[str, Plugin]

    def __init__(self):
        self.__plugins = {}

    def _add_plugin(self, plugin: Plugin):
        self.__plugins[plugin.metadata.entry_point] = plugin

    def get_plugin_by_entry_point(self, entry_point: str) -> Plugin:
        return self.__plugins[entry_point]
    
    def get_all_plugins(self) -> Dict[str, Plugin]:
        return self.__plugins

    @abstractmethod
    def load(self):
        pass
