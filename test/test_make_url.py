'''
testfile for the creation yaml to settings dataclass
'''
import unittest
from yml_config_to_dataclass import make_url

class TestMakeUrl(unittest.TestCase):
    '''
    test class for the yml config to dataclass experiment
    this is is to support me in learning TDD
    '''
    def test_make_url_with_empty_dict(self):
        '''
        test that the function always returns a sdtring even with empty dict
        '''
        test1 = make_url({})
        self.assertIsInstance(test1,str)

    def test_make_url_with_url(self):
        '''
        testcase describe here
        '''
        test1 = make_url({'url':'google.com'})
        self.assertEqual(test1,'google.com')

    def test_make_url_with_protocol(self):
        '''
        testcase describe here
        '''
        test1 = make_url({'url':'google.com',
                          'protocol':'http'})
        self.assertEqual(test1,'http://google.com')

    def test_make_url_with_unsecured_protocol(self):
        '''
        testcase describe here
        '''
        test1 = make_url({'url':'google.com',
                          'protocol':'http',
                          'securred':False})
        self.assertEqual(test1,'http://google.com')
    def test_make_url_with_secured_protocol(self):
        '''
        testcase describe here
        '''
        test1 = make_url({'url':'google.com',
                          'protocol':'http',
                          'secured':True})
        self.assertEqual(test1,'https://google.com')

    def test_make_url_with_unsecured_protocol_and_port(self):
        '''
        testcase describe here
        '''
        test1 = make_url({'url':'google.com',
                          'protocol':'http',
                          'secured':False,
                          'port':8080})
        self.assertEqual(test1,'http://google.com:8080')
    def test_make_url_with_secured_protocol_and_port(self):
        '''
        testcase describe here
        '''
        test1 = make_url({'url':'google.com',
                          'protocol':'http',
                          'secured':True,
                          'port':8080})
        self.assertEqual(test1,'https://google.com:8080')
    def test_make_url_with_secured_protocol_and_port443(self):
        '''
        testcase describe here
        '''
        test1 = make_url({'url':'google.com',
                          'protocol':'http',
                          'secured':True,
                          'port':443})
        self.assertEqual(test1,'https://google.com')
    def test_make_url_with_unsecured_protocol_and_port443(self):
        '''
        testcase describe here
        '''
        test1 = make_url({'url':'google.com',
                          'protocol':'http',
                          'secured':False,
                          'port':443})
        self.assertEqual(test1,'http://google.com:443')

if __name__ == "__main__":
    unittest.main()
