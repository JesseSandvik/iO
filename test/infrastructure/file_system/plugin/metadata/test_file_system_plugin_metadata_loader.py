import unittest

from src.infrastructure.file_system.plugin.metadata.file_system_plugin_metadata_loader import FileSystemPluginMetadataLoader

class TestFileSystemPluginMetadataLoader(unittest.TestCase):
    def setUp(self):
        self.loader = FileSystemPluginMetadataLoader()

    def test_load(self):
        self.loader.load()
        print(self.loader.plugin_metadata)
