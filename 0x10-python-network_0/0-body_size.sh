#!/bin/bash
#print byte size of the HTTP response header for arg URL.
curl -s "$1" | wc -c
