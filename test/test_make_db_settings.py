'''
testfile for make_db_settings
'''

import unittest
from dataclasses import is_dataclass
from yml_config_to_dataclass import make_db_settings, DataBaseItem

class TestMakeDbSettings(unittest.TestCase):
    '''
    test class for make_db_settings
    '''

    def test_make_db_settings(self,):
        '''
        testing so we always get a dataclass of type DataBaseItem
        '''
        test_case = make_db_settings({'timeout':'',
                                      'retry_delay':'',
                                      'app_details':{},
                                      'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',}
                                          }
                                     )
        self.assertIsInstance(test_case, DataBaseItem)
        self.assertTrue(is_dataclass(test_case))

    def test_make_db_settings_for_user_return_type(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_db_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{},
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertIsInstance(test_case.user, str)

    def test_make_db_settings_for_user_return_(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_db_settings({'account':{
                                          'username':'testuser',
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{},
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.user, 'testuser')

    def test_make_db_settings_for_secret_set(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_db_settings({'account':{
                                          'password':'testpassword',
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{},
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.secret, 'testpassword')

    def test_make_db_settings_for_collecting_secret(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_db_settings({'account':{
                                          'username':'testuser',
                                          'password':'',
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{},
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.secret, 'collected_secret')

    def test_make_db_settings_for_blank_database(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_db_settings({'account':{
                                          'username':'testuser',
                                          'password':'',
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{},
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.database, '')

    def test_make_db_settings_for_set_database(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_db_settings({'account':{
                                          'username':'',
                                          'password':'',
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'database':'testdb'
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.database, 'testdb')

    def test_make_db_settings_for_unset_port(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_db_settings({'account':{
                                          'username':'',
                                          'password':'',
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'database':'testdb'
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.port, 3306)

    def test_make_db_settings_for_set_port(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_db_settings({'account':{
                                          'username':'',
                                          'password':'',
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'port':5000
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.port, 5000)

    def test_make_db_settings_for_unset_url(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_db_settings({'account':{
                                          'username':'',
                                          'password':'',
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':''
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.url, '')

    def test_make_db_settings_for_set_url(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_db_settings({'account':{
                                          'username':'',
                                          'password':'',
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':'mydb_url'
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.url, 'mydb_url')

    def test_make_db_settings_keyerror_exeption(self,):
        '''
        empty password and no password_store_username &
        password_store_group shall raise a keyerror
        '''
        self.assertRaises(KeyError,
                          make_db_settings,
                          {})

if __name__ == "__main__":
    unittest.main()
