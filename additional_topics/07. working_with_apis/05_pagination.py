# This program shows how to handle paginated API responses.
# It fetches multiple pages of data.

import requests

base_url = 'https://jsonplaceholder.typicode.com/posts'

for page in range(1, 4):

    print(page)
    
    params = {'_page': page, '_limit': 5}

    response = requests.get(base_url, params=params)

    print(f'Page {page}:', response.json())
    
    print('---')
    print('\n'*3)


'https://jsonplaceholder.typicode.com/posts!_page=1&_limit=5'