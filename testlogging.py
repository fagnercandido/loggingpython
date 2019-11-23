import logging

#logging.basicConfig(filename='test.log', filemode='w', level=logging.DEBUG)#put message inside a file

logging.warning('this a message of warning')
logging.info('this a message of info') #but this message not show, because, default level is warning


logging.debug('this message go to log')
logging.info('too')
logging.warning('And too')