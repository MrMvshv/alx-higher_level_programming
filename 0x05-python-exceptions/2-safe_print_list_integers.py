#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while (x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (ValueError, TypeError):
            pass
        finally:
            i += 1
            x -= 1
    print()
    return i
