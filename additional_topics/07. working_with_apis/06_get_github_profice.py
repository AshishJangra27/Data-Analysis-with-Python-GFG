

# This program fetches GitHub user details given a username or profile link (no Flask).
# It prints followers, repositories, stars, forks, and recent contributions.

import requests

def extract_github_username(url_or_username):
    return url_or_username.split('/')[-1]



def fetch_github_user_details(user_input):
    
    username = extract_github_username(user_input)

    user_url = f'https://api.github.com/users/{username}'
    repos_url = f'https://api.github.com/users/{username}/repos'
    

    user_resp = requests.get(user_url)
    repos_resp = requests.get(repos_url)

    if user_resp.status_code != 200:
        print('GitHub user not found.')
        return

    user_data = user_resp.json()
    repos_data = repos_resp.json() if repos_resp.status_code == 200 else []

    total_stars = sum(repo.get('stargazers_count', 0) for repo in repos_data)
    total_forks = sum(repo.get('forks_count', 0) for repo in repos_data)
    repo_count = len(repos_data)

    events_url = f'https://api.github.com/users/{username}/events/public'
    events_resp = requests.get(events_url)
    contributions = len(events_resp.json()) if events_resp.status_code == 200 else 'N/A'

    print('GitHub User Details:')
    print('Login:', user_data.get('login'))
    print('Name:', user_data.get('name'))
    print('Followers:', user_data.get('followers'))
    print('Following:', user_data.get('following'))
    print('Public Repos:', user_data.get('public_repos'))
    print('Repo Count:', repo_count)
    print('Total Stars:', total_stars)
    print('Total Forks:', total_forks)
    print('Recent Contributions (public events):', contributions)
    print('Profile URL:', user_data.get('html_url'))
    print('Avatar URL:', user_data.get('avatar_url'))

if __name__ == '__main__':
    user_input = input('Enter GitHub username or profile link: ')
    fetch_github_user_details(user_input)
