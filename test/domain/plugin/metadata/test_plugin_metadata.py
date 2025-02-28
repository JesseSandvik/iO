import unittest

from src.domain.plugin import PluginMetadata

class TestPluginMetadata(unittest.TestCase):

    def setUp(self):
        self.plugin_metadata = PluginMetadata(
            name="Test Plugin",
            description="This is for testing purposes.",
            version="1.0.0",
            author="Walter White",
            entry_point="test.main",
            required_python_version="3.10",
        )

    def test_should_generate_plugin_id_on_initialization(self):
        plugin_id = self.plugin_metadata.plugin_id
        self.assertTrue(plugin_id)

    def test_should_generate_last_updated_on_initialization(self):
        last_updated = self.plugin_metadata.last_updated
        self.assertTrue(last_updated)
