#!/usr/bin/python3
"""
 fetches https://alx-intranet.hbtn.io/status using urllib
"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    data = response.read()
print("Body response:")
print("\t- type: ", end="")
print(type(data))
print("\t- content: ", end="")
print(data)
print("\t- utf8 content: ", end="")
print(data.decode("utf-8"))
