# This program shows how to make a basic GET request to an API using `requests`.
# It fetches data from a public API and prints the response.
#
#   - 200 OK: The request succeeded and the server returned the requested data.
#   - 201 Created: A resource was successfully created (common for POST).
#   - 204 No Content: The request succeeded but there's no content to return (common for DELETE).
#
#   - 301 Moved Permanently: The resource has a new URL.
#   - 302 Found / 307 Temporary Redirect: Temporary redirect to a different URL.
#
#   - 400 Bad Request: The request was malformed or invalid.
#   - 401 Unauthorized: Authentication is required or failed.
#   - 403 Forbidden: Authenticated but not allowed to access the resource.
#   - 404 Not Found: The requested resource does not exist.
#   - 429 Too Many Requests: Rate limiting; back off and retry later.
#
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url)

print('Status code:', response.status_code)
print('Response JSON:', response.json())
