def f1(x):
    return x + 10


def f2(x):
    x_sqr = x * x
    return x_sqr - 5


def f3(x):
    x_cube = x * x * x
    return 3 * x_cube


print f1(5) == 15
print f1(27) == 37

print f2(2) == -1
print f2(12) == 139

print f3(2) == 24
print f3(12) == 5184


def three_part(x):
    if x > 20:
        return f1(x)
    if x < 0:
        return f2(x)
    if x == 15:
        return f3(x)
    else :
        return None


print three_part(21) == 31
print three_part(1000) == 1010

print three_part(-1) == -4
print three_part(-5) == 20
print three_part(-5) == f2(-5)

print three_part(15) == 10125
print three_part(15) == f3(15)

print three_part(0) == None
print three_part(16) == None
