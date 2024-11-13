import unittest
import yml_config_to_dataclass

class TestConfigToDataClass(unittest.TestCase):
    '''
    test class for the yml config to dataclass experiment
    this is is to support me in learning TDD
    '''
    def test_get_str_from_empty_dict(self):
        '''
        test we get the cprrect return
        '''
        test1 = yml_config_to_dataclass.make_url_tdd({})
        self.assertIsInstance(test1,str)
