def square(x):
    return x * x


input = 3
print square(input)

input_squared = square(input)

print square(input) * input_squared
print square(input_squared)
print square(square(input))


def add(x1,x2):
    return x1 + x2
x1 = 3
x2 = 4

print add(x1,x2)

sum = add(x1, x2)

print sum

def fancy_division(num, denom):
    quotient = num / denom
    remainder = num % denom

    return


# fancy_division(4, 3) => "4 / 3 is 1 with remainder of 1"
print fancy_division(4, 3)
