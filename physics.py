# delta stands for displacement or change in position
def calc_vel_pos(time, final_pos, initial_pos=0):
    delta = final_pos - initial_pos
    return delta / float(time)


def calc_pos_vel(time, vel, initial_pos=0):
    return vel * time + initial_pos


def calc_acc_vel(time, final_vel, initial_vel=0):
    delta_vel = final_vel - initial_vel
    return delta_vel / float(time)


def calc_vel_acc(time, acc, initial_vel):
    return time * acc + initial_vel


print calc_vel_pos(10, 300, 200) == 10.0
print calc_vel_pos(10, 300) == 30.0
print calc_vel_pos(10, 5, 4) == 0.1

print calc_pos_vel(2, 5, 10) == 20.0
print calc_pos_vel(4, 13, 12) == 64.0
print calc_pos_vel(2.5, 3) == 7.5

print calc_acc_vel(3, 20, 5) == 5.0
print calc_acc_vel(100, 50) == 0.5

print calc_vel_acc(4, 3, 2) == 14.0
print calc_vel_acc(10, 5, 5) == 55.0
