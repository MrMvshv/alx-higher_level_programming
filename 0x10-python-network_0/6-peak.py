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

    start = 0
    end = size - 1
    while (start < end):
        mid = (start + end) // 2
        if (lint[mid] <= lint[mid + 1]):
            start = mid + 1
        else:
            end = mid
    return lint[start]
