

# delta stands for displacement or change in position
def calc_vel_pos(time, final_pos, initial_pos=0):
    delta_pos = final_pos - initial_pos
    return delta_pos / float(time)


def calc_fpos_vel(time, avg_vel, initial_pos=0):
    return avg_vel * time + initial_pos


def calc_acc_vel(time, final_vel, initial_vel=0):
    delta_vel = final_vel - initial_vel
    return delta_vel / float(time)


def calc_fvel_acc(time, acc, initial_vel=0):
    return time * acc + initial_vel


def calc_fpos_acc(time, acc, initial_vel=0, initial_pos=0):
    final_vel = calc_fvel_acc(time, acc, initial_vel)
    avg_vel = (final_vel + initial_vel) / 2
    fpos = avg_vel * time + initial_pos
    return fpos


