'''
testfile for the creation yaml to settings dataclass
'''
import unittest
import os
from unittest.mock import patch
from settings import locate_file

class TestConfigToDataClass(unittest.TestCase):
    '''
    test class for the yml config to dataclass experiment
    this is is to support me in learning TDD
    '''
    @patch('os.path.exists')
    def test_locate_file_file_not_found(self, mock_exists):
        '''
        tests for the function locate_file
        '''
        mock_exists.return_value = False
        self.assertRaises(FileNotFoundError,
                          locate_file,
                          'file_dont_exists.txt')

    @patch('os.path.exists')
    def test_locate_file_return_type(self, mock_exists):
        '''
        tests for the function locate_file
        '''
        # Mock os.path.exists to return True when checking for the specific file
        mock_exists.side_effect = lambda path: path == os.path.join(os.getcwd(),
                                                                    'config/settings.ini')

        test1 = locate_file(file_name='config/settings.ini')
        self.assertIsInstance(test1, str)

if __name__ == "__main__":
    unittest.main()
