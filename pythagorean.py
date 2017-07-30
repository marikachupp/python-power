import math


def square(x):
    return x * x


def add(x1,x2):
    return x1 + x2


def pythag(a, b):
    a_2 = square(a)
    b_2 = square(b)
    c_2 = a_2 + b_2
    c = math.sqrt(c_2)
    return c


print pythag(3,4)
print pythag(6,14)
