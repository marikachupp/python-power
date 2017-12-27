from learning_vectors import Vector


def move_ball(ball, delta_t_sec):
    vel_x = ball.vel.x
    vel_y = ball.vel.y
    og_pos_x = ball.pos.x
    og_pos_y = ball.pos.y

    new_pos_x = og_pos_x + vel_x * delta_t_sec
    new_pos_y = og_pos_y + vel_y * delta_t_sec

    pos = Vector(new_pos_x, new_pos_y)
    vel = Vector(vel_x, vel_y)

    return Ball(pos, vel)


class Ball:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
