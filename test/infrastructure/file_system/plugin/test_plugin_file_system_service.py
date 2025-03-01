import os
import unittest

from src.infrastructure.file_system.plugin.plugin_file_system_service import PluginFileSystemService, PluginFileSystemSettings

class TestPluginFileSystemService(unittest.TestCase):

    def test_get_project_root_directory(self):
        project_root_directory = PluginFileSystemService().get_project_root_directory()
        self.assertEqual(project_root_directory, os.getcwd())
