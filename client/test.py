import requests
import json


url = 'http://127.0.0.1:8000/obtain-auth-token'
obj = {'username':'user', 'password':'password'}
r = requests.post(url, data=obj)
d = r.json()
print(d['token'])
print('=========================')

url = 'http://127.0.0.1:8000/hello?format=json'
token = d['token']
headers = {'Authorization': f'Token {token}'}
r = requests.get(url, headers=headers)
print(r.text)
