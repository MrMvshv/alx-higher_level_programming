#!/usr/bin/python3
"""
 sends a request and displays value of var in header of response
 using requests
"""
if __name__ == "__main__":
    import requests
    import sys

    response = requests.get(sys.argv[1])
    header = response.headers['X-Request-Id']
    print(header)
