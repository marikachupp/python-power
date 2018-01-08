from learning_vectors import Vector
from physics import calc_fpos_vel


def move_ball(ball, delta_t_sec):
    vel_x = ball.vel.x
    vel_y = ball.vel.y
    og_pos_x = ball.pos.x
    og_pos_y = ball.pos.y

    new_pos_x = calc_fpos_vel(delta_t_sec, vel_x, og_pos_x)
    new_pos_y = calc_fpos_vel(delta_t_sec, vel_y, og_pos_y)

    pos = Vector(new_pos_x, new_pos_y)
    vel = Vector(vel_x, vel_y)

    return Ball(pos, vel, ball.rad)


class Ball:
    def __init__(self, pos, vel, rad):
        self.pos = pos
        self.vel = vel
        self.rad = rad


