import math


def pythag(a, b):
    a_2 = a * a
    b_2 = b * b
    c_2 = a_2 + b_2
    c = math.sqrt(c_2)
    return c


print pythag(3, 4) == 5.0
print pythag(6, 8) == 10.0
