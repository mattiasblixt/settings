'''
dataclass entry for our settings
https://www.datacamp.com/tutorial/python-data-classes
'''
from dataclasses import field, dataclass

@dataclass
class ApplicationItem:
    '''
    dataclass for the subsection handling application settings
    '''
    user: str = field(default='')
    secret: str = field(repr=True, default='') #repr=False ensures that secret is not printed
    url: str = field(default='')
    timeout: int = field(default=400)
    retry_delay: list = field(default_factory=lambda: [60,120,180])

@dataclass
class DataBaseItem:
    '''
    dataclass for the subsection handling database settings
    '''
    user: str = field(default='')
    secret: str = field(repr=False, default='') #repr=False ensures that secret is not printed
    url: str = field(default='')
    database: str = field(default='')
    port: int = field(default=3306)
    timeout: int = field(default=400)
    retry_delay: list = field(default_factory=lambda: [60,120,180])

@dataclass
class SettingsItem:
    '''
    dataclass made up for dataclasses for all our settings
    '''
    app: ApplicationItem
    db: DataBaseItem
