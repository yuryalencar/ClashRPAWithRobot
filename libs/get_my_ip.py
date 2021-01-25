from requests import get
from logging import debug, error, info

def get_this_external_machine_ip():
    info('Getting my External IP')

    try:
        external_ip = get('https://api.ipify.org').text
        debug('external_ip-' + external_ip)
        
        return external_ip
    except:
        error('error to get my external api')
        return None