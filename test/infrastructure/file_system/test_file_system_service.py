import os
import unittest

from src.infrastructure.file_system import FileSystemService

class TestFileSystemService(unittest.TestCase):

    def test_get_yaml_file_content(self):
        yaml_file_path = os.path.join(
            os.getcwd(),
            'test',
            'infrastructure',
            'file_system',
            'resources',
            'test.yaml'
        )
        yaml_file_content = FileSystemService.get_yaml_file_contents(yaml_file_path)
        self.assertEqual(yaml_file_content['first_key'], 'value 1')
