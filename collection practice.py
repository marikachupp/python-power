def has_even(list):
    for x in list:
        if x % 2 == 0:
            return True
    return False


print has_even((2, 4, 6, 8)) == True
print has_even((1, 3, 11, 13)) == False
print has_even((1, 2, 3, 4)) == True
