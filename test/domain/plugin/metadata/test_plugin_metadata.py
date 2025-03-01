import unittest

from src.domain.plugin import PluginMetadata

class TestPluginMetadata(unittest.TestCase):

    def setUp(self):
        self.plugin_metadata = PluginMetadata(
            name="Test Plugin",
            description="This is for testing purposes.",
            version="1.0.0-alpha",
            author="Walter White",
            entry_point="test.main",
            required_python_version="3.10",
            compatible_application_versions=["1.0.0","1.0.1"]
        )

    def test_should_generate_plugin_id_on_initialization(self):
        plugin_id = self.plugin_metadata.plugin_id
        self.assertTrue(plugin_id)

    def test_should_generate_last_updated_on_initialization(self):
        last_updated = self.plugin_metadata.last_updated
        self.assertTrue(last_updated)

    def test_version_changed_should_return_true_for_older_version(self):
        actual = self.plugin_metadata.version_changed("0.9.0")
        self.assertTrue(actual)

    def test_version_changed_should_return_true_for_beta_version(self):
        actual = self.plugin_metadata.version_changed("1.0.0-beta")
        self.assertTrue(actual)

    def test_version_changed_should_return_true_for_newer_version(self):
        actual = self.plugin_metadata.version_changed("1.0.1")
        self.assertTrue(actual)

    def test_version_changed_should_return_false_for_same_version(self):
        actual = self.plugin_metadata.version_changed(self.plugin_metadata.version)
        self.assertFalse(actual)

    def test_has_compatible_python_version_should_return_false_for_older_version(self):
        actual = self.plugin_metadata.has_compatible_python_version("3.9")
        self.assertFalse(actual)

    def test_has_compatible_python_version_should_return_true_for_same_version(self):
        actual = self.plugin_metadata.has_compatible_python_version(self.plugin_metadata.required_python_version)
        self.assertTrue(actual)

    def test_has_compatible_python_version_should_return_true_for_newer_version(self):
        actual = self.plugin_metadata.has_compatible_python_version("3.11")
        self.assertTrue(actual)

    def test_has_compatible_python_version_should_return_true_for_newer_minor_version(self):
        actual = self.plugin_metadata.has_compatible_python_version("3.10.1")
        self.assertTrue(actual)

    def test_has_compatible_application_version_should_return_true_compatible_application_version(self):
        actual = self.plugin_metadata.has_compatible_application_version("1.0.1")
        self.assertTrue(actual)

    def test_has_compatible_application_version_should_return_false_incompatible_higher_application_version(self):
        actual = self.plugin_metadata.has_compatible_application_version("1.0.2")
        self.assertFalse(actual)

    def test_has_compatible_application_version_should_return_false_incompatible_lower_application_version(self):
        actual = self.plugin_metadata.has_compatible_application_version("0.9.9")
        self.assertFalse(actual)

    def test_has_compatible_application_version_should_return_false_incompatible_beta_application_version(self):
        actual = self.plugin_metadata.has_compatible_application_version("1.0.0-beta")
        self.assertFalse(actual)
