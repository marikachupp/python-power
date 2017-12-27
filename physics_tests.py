from physics import calc_fpos_acc, calc_vel_pos, calc_fpos_vel, calc_acc_vel, calc_fvel_acc


def is_close(value_one, value_two):
    import math
    return "testing if %1.2f equals %1.2f: %s" % (value_one, value_two, math.fabs(value_one - value_two) < 0.010)

print is_close(calc_fpos_acc(3, -9.81), -44.14)
print is_close(calc_fpos_acc(3, -9.81, -10), -74.14)
print is_close(calc_fpos_acc(3, -9.81, -10, 12), -62.14)

print is_close(calc_vel_pos(10, 300, 200), 10.0)
print is_close(calc_vel_pos(10, 300), 30.0)
print is_close(calc_vel_pos(10, 5, 4), 0.1)

print is_close(calc_fpos_vel(2, 5, 10), 20.0)
print is_close(calc_fpos_vel(4, 13, 12), 64.0)
print is_close(calc_fpos_vel(2.5, 3), 7.5)

print is_close(calc_acc_vel(3, 20, 5), 5.0)
print is_close(calc_acc_vel(100, 50), 0.5)

print is_close(calc_fvel_acc(4, 3, 2), 14.0)
print is_close(calc_fvel_acc(10, 5, 5), 55.0)

