import requests
import json
import pprint
from base64 import b64encode

client_id = '5e99e385-8df4-44cd-935a-c7cb9181e382'
datacenter_url = 'https://eu-cloud.acronis.com'
endpoint = f'{datacenter_url}/api/2/{client_id}'
client_secret = 'bkgvqpkjellf34ost6ib5du2cqhbc2gu7enpvwvpljeipe5c5ehi'
base_url = f'{datacenter_url}/api/2'
print(base_url)
encoded_client_creds = b64encode(f'{client_id}:{client_secret}'.encode('ascii'))
basic_auth = {
    'Authorization': 'Basic ' + encoded_client_creds.decode('ascii')
}
print(basic_auth)

response = requests.post(
     f'{base_url}/idp/token',
     headers={'Content-Type': 'application/x-www-form-urlencoded', **basic_auth},
     data={'grant_type': 'client_credentials'},
 )
token_info = response.json()
auth = {'Authorization': 'Bearer ' + token_info['access_token']}

task_base = 'https://eu-cloud.acronis.com/api/task_manager/v2'
response = requests.get(f'{task_base}/tasks', headers=auth)
print(response.text)