#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while (i < x):
        try:
            if(my_list[i].isdigit()):
                print("{:d}".format(my_list[i]))
                count += 1
        except(IndexError, ValueError, TypeError):
                break
            i += 1
        print("")
        return count
