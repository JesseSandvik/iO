import os
import unittest

from src.infrastructure.file_system.plugin.metadata.file_system_plugin_metadata_loader import FileSystemPluginMetadataLoader

class TestFileSystemPluginMetadataLoader(unittest.TestCase):

    def test_load_directory_without_plugins(self):
        path_without_plugins = os.path.join(
            os.getcwd(),
            'test',
            'infrastructure',
            'file_system',
            'plugin',
            'resources',
            'empty'
        )
        loader = FileSystemPluginMetadataLoader(path_without_plugins)
        loader.load()
        self.assertEqual(len(loader.get_all_plugin_metadata().keys()), 0)

    def test_load_directory_with_plugins(self):
        test_plugins_path = os.path.join(
            os.getcwd(),
            'test',
            'infrastructure',
            'file_system',
            'plugin',
            'resources'
        )
        loader = FileSystemPluginMetadataLoader(test_plugins_path)
        loader.load()
        self.assertEqual(len(loader.get_all_plugin_metadata().keys()), 3)
