#!/usr/bin/python3
"""
post an email to a url, display response using requests
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    response = requests.post(url, data=email)
    body = response.text
    print(body)
