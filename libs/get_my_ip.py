from requests import get

def get_this_external_machine_ip():
    external_ip = get('https://api.ipify.org').text
    return external_ip