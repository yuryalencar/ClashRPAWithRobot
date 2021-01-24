import csv
from requests import get

def make_clan_informations_csv(token, api_url, clan_name, locationId, tag_start):
    headers = { 'Authorization': 'Bearer ' + token }
    payload = {'name': 'The resistance', 'locationId': 57000038}
    url = api_url + 'clans'

    response = get(url, headers=headers, params=payload)
    full_tag = find_full_tag_clan(response.json()['items'], tag_start)

    url = api_url + 'clans/' + full_tag.replace('#', '%23') + '/members'
    response = get(url, headers=headers)

    rows = format_members_to_csv(response.json()['items'])
    save_csv('the_resistence_members', rows)

def find_full_tag_clan(clans, tag_start):
    tag = tag_start.replace("%23", "#")
    tag_length = len(tag)
    for clan in clans:
        if(clan['tag'][0:tag_length] == tag):
            return clan['tag']

    return None

def format_members_to_csv(members):
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
    with open('generated/csv/' + filename + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)