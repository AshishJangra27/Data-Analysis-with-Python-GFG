# This program shows how to send data to an API using a POST request.
# It sends JSON data and prints the response.

import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post(url, json=data)

print('Status code:', response.status_code)
print('Response JSON:', response.json())

# 201 Created: A resource was successfully created (common for POST).