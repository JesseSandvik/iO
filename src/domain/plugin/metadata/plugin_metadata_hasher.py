from abc import ABC, abstractmethod

from .plugin_metadata import PluginMetadata

class PluginMetadataHasher(ABC):

    @abstractmethod
    def hash_metadata(self, metadata: PluginMetadata):
        pass
