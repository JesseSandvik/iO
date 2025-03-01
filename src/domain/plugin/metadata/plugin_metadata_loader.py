from abc import ABC, abstractmethod

class PluginMetadataLoader(ABC):

    @abstractmethod
    def load(self):
        pass
