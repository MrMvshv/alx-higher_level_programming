#!/usr/bin/python3
"""
takes in a letter, sends POST request with letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        data = response.json()
        if data:
            rId = data.get('id')
            rName = data.get('name')
            print("[{}] {}".format(rId, rName))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
