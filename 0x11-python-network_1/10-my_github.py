#!/usr/bin/python3
"""
connect to github and display id using basic auth params
"""
if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        uId = data.get('id')
        print(f"{uId}")
    else:
        print("None")
