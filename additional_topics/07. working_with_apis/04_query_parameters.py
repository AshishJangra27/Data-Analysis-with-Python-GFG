# This program shows how to use query parameters in API requests.
# It sends a GET request with parameters and prints the response.

import requests

url = 'https://jsonplaceholder.typicode.com/comments'
params = {'postId': 1}
response = requests.get(url, params=params)

print('Status code:', response.status_code)
print('Response JSON:', response.json())
