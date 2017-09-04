# delta stands for displacement or change in position
def velocity(time, final_pos, initial_pos=0):
    delta = final_pos - initial_pos
    return delta / float(time)


def final_position(time, vel, initial_pos=0):
    return vel * time + initial_pos


def acceleration(time, final_vel, initial_vel=0):
    delta_vel = final_vel - initial_vel
    return delta_vel / float(time)


def final_velocity(time, acceleration, initial_vel):
    return time * acceleration + initial_vel


print final_velocity(4, 3, 2) == 14.0
print final_velocity(10, 5, 5) == 55.0

print velocity(10, 300, 200) == 10.0
print velocity(10, 300) == 30.0
print velocity(10, 5, 4) == 0.1

print final_position(2, 5, 10) == 20.0
print final_position(4, 13, 12) == 64.0
print final_position(2.5, 3) == 7.5

print acceleration(3, 20, 5) == 5.0
print acceleration(100, 50) == 0.5
