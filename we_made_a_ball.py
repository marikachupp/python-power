def move_ball(ball, delta_t_sec):
    og_vel_x = ball.vel_x
    og_vel_y = ball.vel_y
    og_pos_x = ball.delta_x
    og_pos_y = ball.delta_y

    new_delta_x = og_pos_x + og_vel_x * delta_t_sec
    new_delta_y = og_pos_y + og_vel_y * delta_t_sec

    return Ball(new_delta_x, new_delta_y, og_vel_x, og_vel_y)


class Ball:
    def __init__(self, x, y, velx, vely):
        self.delta_x = x
        self.delta_y = y
        self.vel_x = velx
        self.vel_y = vely
