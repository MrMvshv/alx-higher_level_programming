#!/usr/bin/python3
import sys


def madd():
    sum = 0
    a = len(sys.argv)
    if a == 1:
        print("0")
    elif a == 2:
        print("{}".format(sys.argv[1]))
    else:
        for x in range(1, a):
            sum += int(sys.argv[x])
        print("{}".format(sum))


if __name__ == '__main__':
    madd()
