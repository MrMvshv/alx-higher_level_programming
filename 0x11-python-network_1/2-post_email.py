#!/usr/bin/python3
"""
post an email to a url, display response
"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')
with urllib.request.urlopen(sys.argv[1]) as response:
    body = response.read().decode(utf-8)
print(body)
