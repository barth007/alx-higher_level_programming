#!/usr/bin/python3
# 0-add_integer.py

def add_integer(a, b=98):
    """compute two integers

       Args:
          a(int): the first operand
          b(int): the second operand
      Return:
          a + b
      raise:
          TypeError
    """

    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    elif any(isinstance(x, float) for x in (a, b)):
        result = int(a) + int(b)
    else:
        result = a + b
    return (result)
