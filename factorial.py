# fact short for factorial

def fact(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print fact(-2) == 0
print fact(-1) == 0
print fact(0) == 0
print fact(1) == 1
print fact(2) == 2
print fact(3) == 6
print fact(4) == 24
print fact(5) == 120
