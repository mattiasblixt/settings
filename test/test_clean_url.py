'''
testfile for the creation yaml to settings dataclass
'''
import unittest
from settings import clean_url

class TestMakeUrl(unittest.TestCase):
    '''
    test class for the yml config to dataclass experiment
    this is is to support me in learning TDD
    '''
    def test_make_url_with_empty_str(self):
        '''
        test that the function raises a ValueError with empty string
        '''
        self.assertRaises(ValueError,
                          clean_url,
                          '')

    def test_make_url_with_unsupported_protocol(self):
        '''
        test that the function raises a ValueError if unsupported protocol
        '''
        self.assertRaises(ValueError,
                          clean_url,
                          'ssh://localhost')      

    def test_make_url_with_supported_protocol_http(self):
        '''
        verify we get dict back with shortname + http
        '''
        test_case = clean_url('http://localhost')
        self.assertIsInstance(test_case, dict)

    def test_make_url_with_supported_protocol_https(self):
        '''
        verify we get dict back with shortname + https
        '''
        test_case = clean_url('https://localhost')
        self.assertIsInstance(test_case, dict)

    def test_make_url_with_supported_protocol_ftp(self):
        '''
        verify we get dict back with shortname + ftp
        '''
        test_case = clean_url('ftp://localhost')
        self.assertIsInstance(test_case, dict)

    def test_make_url_with_supported_protocol_ftps(self):
        '''
        verify we get dict back with shortname + ftps
        '''
        test_case = clean_url('ftps://localhost')
        self.assertIsInstance(test_case, dict)

    def test_make_url_specific_dict_values_shortname(self):
        '''
        verify we get dict with correct values back using shortname
        url, protocol
        '''
        test_case = clean_url('ftps://localhost')
        self.assertEqual(test_case,{'url':'localhost',
                                    'protocol':'ftps',
                                    }
                                    )

    def test_make_url_specific_dict_values_fqdn(self):
        '''
        verify we get dict with correct values back
        url, protocol
        '''
        test_case = clean_url('ftps://localhost.de')
        self.assertEqual(test_case,{'url':'localhost.de',
                                    'protocol':'ftps',
                                    }
                                    )

    def test_make_url_specific_dict_values_shortname_port(self):
        '''
        verify we get dict with correct values back
        url, protocol, port
        '''
        test_case = clean_url('ftps://localhost:123')
        self.assertEqual(test_case,{'url':'localhost',
                                    'protocol':'ftps',
                                    'port':123
                                    }
                                    )

    def test_make_url_specific_dict_values_fqdn_adv(self):
        '''
        verify we get dict with correct values back
        url, protocol
        '''
        test_case = clean_url('ftps://localhost.ab.cd.ef')
        self.assertEqual(test_case,{'url':'localhost.ab.cd.ef',
                                    'protocol':'ftps',
                                    }
                                    )

    def test_make_url_specific_dict_values_fqdn_adv_port(self):
        '''
        verify we get dict with correct values back
        url, protocol, port
        '''
        test_case = clean_url('ftps://localhost.ab.cd.ef:123')
        self.assertEqual(test_case,{'url':'localhost.ab.cd.ef',
                                    'protocol':'ftps',
                                    'port':123
                                    }
                                    )

if __name__ == "__main__":
    unittest.main()
