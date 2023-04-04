#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers
peak is number greater than both neighbors
"""


def find_peak(list_of_integers):
    """ finds peak in list_of_integers"""
    lint = list_of_integers

    if lint is None or lint == []:
        return None

    size = len(lint)
    if size == 1:
        return lint[0]

    if lint[0] > lint[1]:
        peak = lint[0]

    end = size - 1
    for i in range(size):
        if lint[i] >= lint[i - 1] and lint[i] >= lint[i + 1]:
            peak = lint[i]
            return peak
        if end != (size - 1):
            if lint[end] >= lint[end + 1] and lint[end] >= lint[end - 1]:
                peak = lint[end]
                return peak
    if end == (size - 1) and lint[end] > lint[end - 1]:
        peak = lint[end]
    return peak
