#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    new = [0 for count in range(list_length)]
    while count < list_length:
        try:
            new[count] = my_list_1[count] / my_list_2[count]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            count += 1
    return (new)
