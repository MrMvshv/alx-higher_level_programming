#!/usr/bin/python3

""" MyList that inherits from list
    print_sorted function
    prints sorted ints
"""


class MyList(list):
    """ inherits from list
        class MyList
    """
    def print_sorted(self):
        """ print_sorted(list)
            prints int list
            in ascending order
        """
        nw = []

        for x in range(len(self)):
            nw.append(self[x])

        nw.sort()
        print(nw)
