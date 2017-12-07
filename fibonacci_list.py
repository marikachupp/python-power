from fibonacci import fibonacci


def fib_list(max_index_num):
    nacci = []
    for index in range(max_index_num + 1):
        value = fibonacci(index)
        print "Fibonacci of", index, "is", value
        nacci.append(value)
    return nacci


print fib_list(6)
# print fib_list(6) == [0, 1, 1, 2, 3, 5, 8]

print fibonacci(5)
print fibonacci(6)
print fibonacci(7)

# max_value = fibonacci(max_index_num)
# print "Fibonacci of", max_index_num, "is", max_value
# return range(max_value)
