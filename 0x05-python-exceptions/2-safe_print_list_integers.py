#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0;
    try:
        for items in range(0, x):
            print("{:d}".format(my_list[items]), end="")
            i += 1
    except ValueError:
        pass
    except IndexError:
        pass

    print()
    return i
