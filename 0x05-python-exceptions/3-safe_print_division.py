#!/usr/bin/python3
def safe_print_division(a, b):
    dif = None
    try:
        dif =  a / b
    except ZeroDivisionError:
        return dif
    finally:
        print("Inside result: {}".format(dif))
    return dif
