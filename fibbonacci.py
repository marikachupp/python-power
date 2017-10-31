def f(x):
    return 0


def f1(x):
    return 1


def f2(x):
    return (x - 1) + (x - 2)


print f(0) == 0
print f(2017) == 0
print f(16) == 0

print f1(5) == 1
print f1(27) == 1
print f1(100002002020) == 1


def fibonacci(x):
    if x == 0:
        return f(x)
    if x == 1:
        return f1(x)
    if x > 1:
        return fibonacci(x - 1) + fibonacci(x - 2)
    else:
        return None


print fibonacci(0) == 0
print fibonacci(1) == 1
print fibonacci(2) == 1
print fibonacci(3) == 2
print fibonacci(4) == 3
print fibonacci(5) == 5
print fibonacci(6) == 8

print fibonacci(-1) == None
print fibonacci(-245) == None
