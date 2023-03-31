#!/usr/bin/python3
"""
 sends a request and displays value of var in header of response
"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    header = response.getheader('X-Request-Id')
print(header)
