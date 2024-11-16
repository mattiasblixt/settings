'''
testbed for making a yaml config to data class settings object
https://www.datacamp.com/tutorial/python-data-classes
'''
import sys
import logging
import settings

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                    #format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
                    #format='%(asctime)s %(name)s %(levelname)s %(lineno)d %(message)s',
                    format='%(asctime)s %(levelname)s %(lineno)d %(message)s',
                    handlers=[logging.StreamHandler(sys.stdout)],
                    )

    app_settings = settings.load_settings()

    logging.info(app_settings)
    logging.info('the stored settings in settings can now be accesses via .(dot) notification')
    logging.info('''example, to access the 'url' for the 'app' part of the''')
    logging.info('''app_settings use: 'app_settings.app.url' and you will get: '%s' ''',
                 app_settings.app.url)
