#!/usr/bin/python3
import sys
a = len(sys.argv)
if a == 1:
    print("0 arguments.")
elif a == 2:
    print("1 argument:\n1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(a-1))
    for x in range(1, a):
        print("{}: {}".format(x, sys.argv[x]))
