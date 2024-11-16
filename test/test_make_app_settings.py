'''
testfile for the creation yaml to settings dataclass
'''
import unittest
from dataclasses import is_dataclass
from settings import make_app_settings, \
                               ApplicationItem

class TestMakeAppSettings(unittest.TestCase):
    '''
    test class for the yml config to dataclass experiment
    this is is to support me in learning TDD
    '''

    def test_make_app_settings_keyerror_exeption(self,):
        '''
        testing so we always get exeption of not corect input
        '''
        self.assertRaises(KeyError,
                          make_app_settings, {})

    def test_make_app_settings_valuerror_one(self,):
        '''
        test so we raise correct errors
        '''
        self.assertRaises(ValueError,
                          make_app_settings,
                          {'account':{},
                          'app_details':'',
                          'timeout':'',
                          'retry_delay':''}
                          )

    def test_make_app_settings_valuerror_two(self,):
        '''
        test so we raise correct errors
        '''
        self.assertRaises(ValueError,
                          make_app_settings,
                          {'account':'',
                          'app_details':{},
                          'timeout':'',
                          'retry_delay':''}
                          )

    def test_make_app_settings(self,):
        '''
        testing so we always get a dataclass of type ApplicationItem
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':''
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertIsInstance(test_case, ApplicationItem)
        self.assertTrue(is_dataclass(test_case))

    def test_make_app_settings_for_user(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':'',
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertIsInstance(test_case.user, str)

    def test_make_app_settings_for_secret(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':''
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertIsInstance(test_case.user, str)

    def test_make_app_settings_for_url(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':''
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertIsInstance(test_case.url, str)

    def test_make_app_settings_for_timeout(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':'',
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertIsInstance(test_case.timeout, int)

    def test_make_app_settings_for_retry_delay(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':''
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertIsInstance(test_case.retry_delay, list)

    def test_make_app_settings_template(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':''
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertIsInstance(test_case, ApplicationItem)
        self.assertTrue(is_dataclass(test_case))

    def test_make_app_settings_user(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_app_settings({'account':{
                                          'username':'appuser',
                                          'password_store_username':'',
                                          'password_store_group':'',
                                       },
                                       'app_details':{
                                           'url':''
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.user,'appuser')

    def test_make_app_settings_url_one(self,):
        '''
        tests so the protocol is return as expected
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':'',
                                           'protocol':'http',
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.url,'http://')

    def test_make_app_settings_url_two(self,):
        '''
        tests so we get a protocol + port return
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':'',
                                           'protocol':'http',
                                           'port':8080,
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.url,'http://:8080')

    def test_make_app_settings_url_three(self,):
        '''
        test so we get a protocol, url and port as expected
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'protocol':'http',
                                           'port':8080,
                                           'url':'google.com'
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.url,'http://google.com:8080')

    def test_make_app_settings_url_four(self,):
        '''
        test so we get a protocol, url and port as expected
        when supplying secured false
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'protocol':'http',
                                           'port':8080,
                                           'url':'google.com',
                                           'secured': False,
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.url,'http://google.com:8080')

    def test_make_app_settings_url_five(self,):
        '''
        test so we get a protocol, url and port as expected
        when supplying secured True
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'protocol':'http',
                                           'port':8080,
                                           'url':'google.com',
                                           'secured': True,
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.url,'https://google.com:8080')

    def test_make_app_settings_url_six(self,):
        '''
        test so we get a protocol, url and port as expected
        when supplying secured True and port 443
        special case
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'protocol':'http',
                                           'port':443,
                                           'url':'google.com',
                                           'secured': True,
                                       },
                                       'timeout':'',
                                       'retry_delay':''})
        self.assertEqual(test_case.url,'https://google.com')

    def test_make_app_settings_timeout(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':'',
                                       },
                                       'timeout':120,
                                       'retry_delay':''})

        self.assertEqual(test_case.timeout,120)

    def test_make_app_settings_retry(self,):
        '''
        boilerplate test docstring template, update before commit
        '''
        test_case = make_app_settings({'account':{
                                          'password_store_username':'',
                                          'password_store_group':'',
                                      },
                                       'app_details':{
                                           'url':'',
                                       },
                                       'timeout':'',
                                       'retry_delay':[35,70,105]})

        self.assertEqual(test_case.retry_delay,[35,70,105])

if __name__ == "__main__":
    unittest.main()
