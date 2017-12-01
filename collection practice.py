import sys


def is_even(x):
    if x % 2 == 0:
        return True
    return False


def any_even(list):
    for x in list:
        if is_even(x):
            return True
    return False


print any_even((2, 4, 6, 8)) == True
print any_even((1, 3, 11, 13)) == False
print any_even((1, 2, 3, 4)) == True


def all_even(list):
    for x in list:
        if not (is_even(x)):
            return False
    return True


print all_even((1, 2, 3)) == False
print all_even((2, 4, 6, 8, 10)) == True
print all_even((2, 4, 5)) == False
print all_even((4, 16, 40, 120, 2000)) == True


def count_even(list):
    total = 0
    for x in list:
        if is_even(x):
            total = total + 1
    return total


print count_even((1, 2, 3, 4)) == 2
print count_even((24, 32, 92, 102)) == 4
print count_even((9, 11, 13)) == 0


def no_even(list):
    for x in list:
        if is_even(x):
            return False
    return True


print no_even((1, 2, 3)) == False
print no_even((1, 1, 1, 7, 9)) == True
print no_even((2, 4, 8, 4, 6)) == False
print no_even((3, 9, 11)) == True
print no_even((2, 1)) == False
print no_even([]) == True


def max_even(list):
    max_num = None
    for x in list:
        if is_even(x):
            if x > max_num:
                max_num = x
    return max_num


print max_even((2, 4, 6, 8)) == 8
print max_even((8, 6, 4, 2)) == 8
print max_even((1, 2, 3, 4, 1)) == 4
print max_even((24, 99, 104, 222, 4)) == 222
print max_even((3, 11, 9)) == None
print max_even([]) == None
print max_even((-2, -4, -8)) == -2


def min_even(list):
    min_num = sys.maxint
    for x in list:
        if is_even(x):
            if x < min_num:
                min_num = x

    if min_num == sys.maxint:
        return None
    return min_num


print min_even((2, 4, 6, 8)) == 2
print min_even((-8, 8, -2, 2)) == -8
print min_even((10, -10, -100)) == -100
print min_even((1, 3, 9, 7, 88, 24)) == 24
print min_even((3, 3, 3, 3)) == None
print min_even([]) == None
