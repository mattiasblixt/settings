'''
testfile for the creation yaml to settings dataclass
'''
import unittest
from settings import load_yml_file

class TestConfigToDataClass(unittest.TestCase):
    '''
    test class for the yml config to dataclass experiment
    this is is to support me in learning TDD
    '''
    def test_load_yml_file(self):
        '''
        tests for the function load_yml_file
        '''
        test1 = load_yml_file(filename='config/global.yml')
        self.assertIsInstance(test1,dict)

    def test_load_yml_file_file_not_found(self):
        '''
        tests for the function load_yml_file
        '''
        self.assertRaises(FileNotFoundError,
                          load_yml_file,
                          'file_dont_exists.txt')

if __name__ == "__main__":
    unittest.main()
