#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    function that divides element by element 2 list
    @my_list_1 & @my_list_2: can contain any type (integer, string)
    """
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1 / my_list_2)
        except ValueError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
