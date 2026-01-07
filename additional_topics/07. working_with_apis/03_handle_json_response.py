# This program shows how to handle JSON responses from an API.
# It parses and prints specific fields from the response.

import requests

url = 'https://jsonplaceholder.typicode.com/users/1'
response = requests.get(url)

print(response.json())
print('-'*20)

if response.status_code == 200:
    data = response.json()
    print('Name:', data['name'])
    print('Email:', data['email'])
else:
    print('Failed to fetch data. Status code:', response.status_code)
