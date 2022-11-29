#!/usr/bin/python3


def to_up(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)


def uppercase(str):
    strings = ""
    for character in str:
        strings += "%c" % to_up(character)
    print("{:s}".format(strings))
