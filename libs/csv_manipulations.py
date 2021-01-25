import csv
from requests import get
from logging import debug, error, info, warn

def make_clan_informations_csv(token, api_url, clan_name, locationId, tag_start):
    headers = { 'Authorization': 'Bearer ' + token }
    payload = {'name': 'The resistance', 'locationId': 57000038}
    url = api_url + 'clans'

    clans = get_clans(url, headers, payload)
    full_tag = find_full_tag_clan(clans.json()['items'], tag_start)

    members = get_members(api_url, headers, full_tag)
    rows = format_members_to_csv(members.json()['items'])

    save_csv('the_resistence_members', rows)

def get_clans(url, headers, payload):
    info('Making request to get full tag')
    debug('url-' + str(url) + '-headers-' + str(headers) + '-params-' + str(payload))
    
    try:
        response = get(url, headers=headers, params=payload)
        return response
    except:
        error('Error in request to get full tag')

def get_members(api_url, headers, tag):
    debug('api_url-' + str(api_url) + '-headers-' + str(headers) + '-tag-' + str(tag))
    
    url = api_url + 'clans/' + tag.replace('#', '%23') + '/members'
    
    try:
        info('Making request to get members')
        debug('url-' + str(url) + '-headers-' + str(headers))
        
        response = get(url, headers=headers)
        return response
    except:
        error('Error in request to get clan members')

def find_full_tag_clan(clans, tag_start):
    info('Finding full tag by partial tag')
    debug('clans-' + str(clans) + '-tag_start-' + str(tag_start))

    tag = tag_start.replace("%23", "#")
    tag_length = len(tag)
    for clan in clans:
        if(clan['tag'][0:tag_length] == tag):
            return clan['tag']

    error('Tag not found')
    return None

def format_members_to_csv(members):
    info('Formating members to save in csv')
    debug('members-' + str(members))
    
    rows = []
    for member in members:
        row = []
        row.append(member['name'])
        row.append(member['expLevel'])
        row.append(member['trophies'])
        row.append(member['role'])
        rows.append(row)

    return rows

def save_csv(filename, data):
    info('Saving csv file')
    debug('filename-' + str(filename) + '-data-' + str(data))
    
    try:
        with open('generated/csv/' + filename + '.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except:
        error('Error to save csv file')