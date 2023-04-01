#!/usr/bin/python3
"""
connect to github and display id using basic auth params
"""
if __name__ == "__main__":
    import requests
    import sys

    repname = sys.argv[1]
    owname = sys.argv[2]

    url = f'https://api.github.com/repos/{owname}/{repname}/commits'

    response = requests.get(url, params={'per_page': 10})

    if response.status_code == 200:
        data = response.json()
        for comm in data:
            print(f"{comm['sha']}: {comm['commit']['author']['name']}")
    else:
        print("Error")
