#!/usr/bin/python3

safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3,"H", 4]
x = len(my_list) - 2
nb_print = safe_print_list_integers(my_list, x)
print("{:d}".format(nb_print))
