#!/usr/bin/python3
# 2-replace_in_list.py


def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)

================================

3-print_reversed_list_integer.p

#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
