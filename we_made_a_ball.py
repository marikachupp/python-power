from learning_vectors import Vector
from physics import calc_fpos_vel


def move_ball(ball, delta_t_sec):
    og_pos_x = ball.pos.x
    og_pos_y = ball.pos.y

    new_pos_x = calc_fpos_vel(delta_t_sec, ball.vel.x, og_pos_x)
    new_pos_y = calc_fpos_vel(delta_t_sec, ball.vel.y, og_pos_y)

    pos = Vector(new_pos_x, new_pos_y)

    return ball.with_pos(pos)


class Ball:
    def __init__(self, pos, vel, rad):
        self.pos = pos
        self.vel = vel
        self.rad = rad

    def with_pos(self, new_pos):
        return Ball(new_pos, self.vel, self.rad)

    def with_vel(self, new_vel):
        return Ball(self.pos, new_vel, self.rad)
