from requests import get
import logging

def get_this_external_machine_ip():
    logging.info('Getting my External IP')
    try:
        external_ip = get('https://api.ipify.org').text
        logging.debug('my ip' + external_ip)
        
        return external_ip
    except:
        logging.error('error to get my external api')
        return None