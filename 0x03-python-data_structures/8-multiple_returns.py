#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        d = 0
        c = None
    else:
        d = len(sentence)
        c = sentence[0]
    tup_s = (d, c)
    return tup_s


if __name__ == '__main__':
    multiple_returns()
