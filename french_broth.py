def calc_is_even(x):
    x_is_even = (x % 2) == 0

    if x_is_even:
        return True
    else:
        return False


def f1(x):
    x_sqr = x * x
    return x_sqr + 5


print f1(5) == 30
print f1(4) == 21


def f2(x):
    return 5 * x + 5


print f2(5) == 30
print f2(4) == 25
print f2(12) == 65


def peace(x):
    if x >= 0:
        return f1(x)
    else:
        return f2(x)


print peace(10) == 105
print peace(-7) == -30
