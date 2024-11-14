'''
testbed for making a yaml config to data class settings object
https://www.datacamp.com/tutorial/python-data-classes
'''
import os
import sys
import logging
from dataclasses import field, dataclass, fields
import yaml

@dataclass
class ApplicationItem:
    '''
    dataclass for the application settings
    for our application
    '''
    user: str = field(default='')
    secret: str = field(repr=True, default='') #repr=False makes the secret not printed
    url: str = field(default='')
    timeout: int = field(default=400)
    retry_delay: list = field(default_factory=lambda: [60,120,180])

@dataclass
class DataBaseItem:
    '''
    dataclass for the application settings
    for our application
    '''
    user: str = field(default='')
    secret: str = field(repr=False, default='') #repr=False makes the secret not printed
    url: str = field(default='')
    database: str = field(default='')
    port: int = field(default=3306)
    timeout: int = field(default=400)
    retry_delay: list = field(default_factory=lambda: [60,120,180])

@dataclass
class SettingsItem:
    '''
    class for all our settings
    '''
    app: ApplicationItem
    db: DataBaseItem

def load_yml_file(filename: str) -> dict:
    """
    This function will load and read a yaml file
    :return: config_settings -> dict_type
    @param filename: filename of a yaml file to be loaded
    @return: Returns a loaded yaml file as dictionary
    """
    try:
        if '/' in filename:
            config_path = os.path.join(os.getcwd(), filename)
        else:
            config_path = os.path.join(os.getcwd(), "config", filename)
        with open(file=config_path, encoding="UTF-8") as file:
            config_settings = yaml.safe_load(file)
            return config_settings
    except FileNotFoundError as ex_fnf:
        logging.error("ERROR: There is no settings file, exiting - %s", ex_fnf)
        raise FileNotFoundError from ex_fnf
    except KeyError as exc_key:
        logging.error("ERROR: cannot find the following key in yml file, exiting - %s ", exc_key)
        return None
    except yaml.YAMLError as exc_yaml:
        logging.error("ERROR: Cannot parse yml file - %s", exc_yaml)
        return None
    except AttributeError as exc_attrib:
        logging.error("ERROR: AttributeError in yml file - %s", exc_attrib)
        return None

def print_data_class(dataclass_instance):
    '''
    dataclass printer
    '''

    # option 1: fields
    all_fields = fields(dataclass_instance)

    # # option 2: inspect
    # members = inspect.getmembers(type(dataclass_instance))
    # fields = list(dict(members)['__dataclass_fields__'].values())

    for v in all_fields:
        logging.info(f'{v.name}: ({v.type.__name__}) = {getattr(dataclass_instance, v.name)}')

def make_url(url_dict: dict) -> str:
    '''
    tdd testing  1 oh 1
    '''
    # TODO add so the function an handle IF the URL already contains a protocl header
    # url_regex = r'(?:(http:|https:|ftp:|ftps:)\/\/)([\w-]+\.+[a-z]{2,24})'
    url = url_dict.get('url','')
    protocol = url_dict.get('protocol','')
    secured = url_dict.get('secured',None)
    port = url_dict.get('port','')
    if len(protocol)> 0:
        if isinstance(port,int):
            #special handling to remove port 443 from https urls
            if protocol == 'http' and secured and port == 443:
                port = ''
            else:
                port = f''':{port}'''
        if secured:
            protocol = f'''{protocol}s'''
        protocol = f'''{protocol}://'''

    return f'''{protocol}{url}{port}'''

def get_secret(in_dict: dict) -> str:
    '''
    future function to collect a secret from a remote secret store
    '''
    secret = in_dict.get('password','')

    if len(secret)>0:
        return secret

    needed_keys = ['password_store_username','password_store_group']
    for item in needed_keys:
        if item not in in_dict:
            raise KeyError(f'''required settings entry '{item}' not in loaded dict''')

    secret = fetch_secret_from_store(in_dict)

    return secret

def fetch_secret_from_store(in_dict:dict) -> str:
    '''
    mock function until such time a passord store is decided
    '''
    return 'collected_secret'

def make_app_settings(in_dict:dict) -> ApplicationItem:
    '''
    makes the application dataclass object
    '''
    data_cls = ApplicationItem()

    needed_keys = ['timeout', 'retry_delay',]
    needed_dict_keys = ['account', 'app_details',]
    for item in needed_keys:
        if item not in in_dict:
            raise KeyError(f'''required settings entry '{item}' not in loaded dict''')

    for item in needed_dict_keys:
        if not isinstance(in_dict.get(item),dict):
            raise ValueError(f'''required settings entry '{item}' is not of type dict''')

    account = in_dict.get('account')
    app_details = in_dict.get('app_details')
    data_cls.user = account.get('username','')
    data_cls.secret = get_secret(account)
    data_cls.url = make_url(app_details)
    timeout = in_dict.get('timeout',None)
    if timeout is not None and isinstance(timeout,int):
        data_cls.timeout = timeout
    retry_delay = in_dict.get('retry_delay',None)
    if retry_delay is not None and isinstance(retry_delay,list):
        data_cls.retry_delay = retry_delay

    return data_cls

def make_db_settings(in_dict:dict) -> DataBaseItem:
    '''
    makes the database dataclass object
    '''
    data_cls = DataBaseItem()
    needed_keys = ['timeout', 'retry_delay',]
    needed_dict_keys = ['account', 'app_details',]
    for item in needed_keys:
        if item not in in_dict:
            raise KeyError(f'''required settings entry '{item}' not in loaded dict''')

    for item in needed_dict_keys:
        if not isinstance(in_dict.get(item),dict):
            raise ValueError(f'''required settings dict entry '{item}' is not of type dict''')

    account = in_dict.get('account')
    data_cls.user = account.get('username','')
    data_cls.secret = get_secret(account)
    app_details = in_dict.get('app_details')

    database = app_details.get('database',None)
    if database is not None and isinstance(database,str):
        data_cls.database = database

    port = app_details.get('port',None)
    if port is not None and isinstance(port,int):
        data_cls.port = port

    url = app_details.get('url',None)
    if url is not None and isinstance(url,str):
        data_cls.url = url

    timeout = app_details.get('timeout',None)
    if timeout is not None and isinstance(timeout,int):
        data_cls.timeout = timeout

    retry_delay = in_dict.get('retry_delay',None)
    if retry_delay is not None and isinstance(retry_delay,list):
        data_cls.retry_delay = retry_delay

    return data_cls

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                    #format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
                    #format='%(asctime)s %(name)s %(levelname)s %(lineno)d %(message)s',
                    format='%(asctime)s %(levelname)s %(lineno)d %(message)s',
                    handlers=[logging.StreamHandler(sys.stdout)],
                    )
    raw_settings = load_yml_file('global.yml')
    execution_settings = raw_settings['dev']

    # inittate the dataclass container with the subparts
    dc_settings = SettingsItem(
        app=ApplicationItem(),
        db=DataBaseItem()
    )
    # loop over all the selected parts of the yaml file and populate the
    # dataclass skeleton with values
    for lkey,lvalue in execution_settings.items():
        if lkey == 'application':
            dc_settings.app = make_app_settings(lvalue)
        if lkey == 'db':
            dc_settings.db = make_db_settings(lvalue)

    logging.info(dc_settings)
    logging.info('the stored settings in dc_settings can now be accesses via .(dot) notification')
    logging.info('''example, to access the 'url' for the 'app' part of the''')
    logging.info('''settings us: 'dc_settings.app.url' and you will get: '%s' ''',
                 dc_settings.app.url)
