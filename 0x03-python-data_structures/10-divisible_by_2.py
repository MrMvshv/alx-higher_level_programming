#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return
    else:
        new_list = []
        for x in my_list:
            if x % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
    return new_list


if __name__ == '__main__':
    print_list_integer([])
