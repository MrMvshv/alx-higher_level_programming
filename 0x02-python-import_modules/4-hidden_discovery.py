#!/usr/bin/python3
import hidden_4


def magombano():
    names = dir(hidden_4)
    for name in names:
        if name[0:2] != "__":
            print("{:s}".format(name))


if __name__ == '__main__':
    magombano()
