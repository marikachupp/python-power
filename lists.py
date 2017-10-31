a = [3, 6, 9]
print a[0]
print a[2]

a.append(12)
a[1] = 7
print a

print [1, 2, 3] + [4, 5, 6]
print [4, 5, 6] + [1, 2, 3]

for x in a:
    print x


def f(num):
    return num * num


for y in a:
    print f(y)


def calc_sum(list):
    total = 0
    for x in list:
        total = total + x
    return total


print calc_sum([]) == 0
print calc_sum(a) == 31
