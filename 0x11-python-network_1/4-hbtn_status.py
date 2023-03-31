#!/usr/bin/python3
"""
 fetches https://alx-intranet.hbtn.io/status using requests
"""
import requests

data = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: ", end="")
print(type(data.text))
print("\t- content: ", end="")
print(data.text)
