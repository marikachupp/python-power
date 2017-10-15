#write a function that returns the sum of all numbers up to x

def f(x):
    x_sqr = x * x
    if x > 0:
        return x_sqr - f(x - 1)
    else:
        return 0


print f(0) == 0
print f(1) == 1
print f(2) == 3
print f(3) == 6
print f(4) == 10
print f(5) == 15
