#/bin/env python3

import json
import re
import requests
import uuid
import sys

def generate_integers(apiKey, num, minimum, maximum, replacement=True):
    request_map = {
        'jsonrpc': '2.0',
        'method': 'generateIntegers',
        'params': {
            'apiKey': apiKey,
            'n': num,
            'min': minimum,
            'max': maximum,
            'replacement': replacement
        },
        'id': uuid.uuid4().hex
    }
    response = requests.post('https://api.random.org/json-rpc/1/invoke',
        data=json.dumps(request_map),
        headers={'content-type': 'application/json'})
    data = response.json()

    if 'error' in data:
        code = int(data['error']['code'])
        message = data['error']['message']
        if code == 401:
            print('Random.org appears to be offline.', file=sys.stderr)
        elif code == 402:
            print('No requests available on this api key.', file=sys.stderr)
        elif code == 403:
            print('No bits available to serve this request.', file=sys.stderr)
        else:
            print('Request returned error: {}'.format(message), file=sys.stderr)
        sys.exit(1)

    return map(int, data['result']['random']['data'])

apiKey = None
with open("config/api.key", 'r') as apiFile:
    apiKey = apiFile.read()
    apiKey = re.sub(r'[\n]', '', apiKey)

if apiKey is None:
    print('Could not find api key to use on Random.org', file=sys.stderr)
    sys.exit(1)

random_list = generate_integers(apiKey, 5, 1, 6 * 6)
random_list = map(str, random_list)
for i in range(0, 6):



file_request = requests.get('https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt')
if (file_request.status_code != 200):
    print('Could not connect to EFF to download password list', file=sys.stderr)
    sys.exit(1)

dict_lines = file_request.text.split('\n')
dict_lines = [line for line in dict_lines if '\t' in line]
password_dict = {key : value for key, value in map(lambda x: x.split('\t'), dict_lines)}

password_parts = [password_dict[dice_roll] for dice_roll in dice_rolls]
password = ''.join(password_parts)

print('Password is {}'.format(password))
