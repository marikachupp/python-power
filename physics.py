# delta stands for displacement or change in position
def velocity(time, x2, x1=0):
    delta = x2 - x1
    return delta / time


print velocity(10, 300, 200) == 10.0
print velocity(10, 300) == 30.0
