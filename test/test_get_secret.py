'''
testfile for the creation yaml to settings dataclass
'''
import unittest
from yml_config_to_dataclass import get_secret

class TestGetSecret(unittest.TestCase):
    '''
    test class for the yml config to dataclass experiment
    this is is to support me in learning TDD
    '''

    def test_get_secret_empty_dict(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        self.assertRaises(KeyError,
                          get_secret, {})

    def test_get_secret_submitted_password(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = get_secret({'password':'secret_password'})
        self.assertEqual(test_case,'secret_password')

    def test_get_secret_keyerror_exeption(self,):
        '''
        empty password and no password_store_username &
        password_store_group shall raise a keyerror
        '''
        self.assertRaises(KeyError,
                          get_secret,
                          {'password':''})

    def test_get_secret_four(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = get_secret({'password':'',
                                'password_store_username':'',
                                'password_store_group':''})
        self.assertEqual(test_case,'collected_secret')

    def fetch_secret_from_store(self,):
        '''
        to test the mock funktion fetch_secret_from_store that always
        should return a str ('collected_secret')
        '''
        test_case = get_secret({})
        self.assertIsInstance(test_case, str)

if __name__ == "__main__":
    unittest.main()