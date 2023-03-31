#!/usr/bin/python3
"""
display response body, handling errors
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
