'''
testfile for the creation yaml to settings dataclass
'''
import unittest
from unittest.mock import mock_open, patch
from yml_config_to_dataclass import load_ini_file

class TestConfigToDataClass(unittest.TestCase):
    '''
    test class for the yml config to dataclass experiment
    this is is to support me in learning TDD
    '''
    def test_load_ini_file_file_not_found(self):
        '''
        tests for the function load_yml_file
        '''
        self.assertRaises(FileNotFoundError,
                          load_ini_file,
                          'file_dont_exists.txt')

    def test_load_ini_file_return_type(self):
        '''
        tests for the function load_yml_file
        '''
        mock_file_content = "envirotargetnment=dev\n"
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            test1 = load_ini_file(filename='config/settings.ini')
            self.assertIsInstance(test1, dict)

    def test_load_ini_file_return_value(self):
        '''
        tests for the function load_yml_file
        '''
        mock_file_content = "target=dev\n"
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            test1 = load_ini_file(filename='config/settings.ini')
            self.assertEqual(test1, {'target':'dev'})

if __name__ == "__main__":
    unittest.main()
