from learning_vectors import Vector
from we_made_a_ball import move_ball, Ball

BALL_RADIUS = 50


def initialize_ball():
    return Ball(pos=Vector(0, 0), vel=Vector(150, 30), rad=BALL_RADIUS)


# returns instance of Ball
def calculate_new_ball(ball, delta_t_ms, width, height):
    delta_t_sec = delta_t_ms / 1000.0

    updated_ball = move_ball(ball, delta_t_sec)
    new_pos_x = updated_ball.pos.x
    new_pos_y = updated_ball.pos.y

    diameter = (2 * ball.rad)
    print new_pos_x, new_pos_y, diameter

    if (0 >= new_pos_x) or (new_pos_x + diameter >= width):
        vel_x = updated_ball.vel.x * -1
        vel_y = updated_ball.vel.y
        vel = Vector(vel_x, vel_y)
        return updated_ball.with_vel(vel)

    if (0 >= new_pos_y) or (new_pos_y + diameter >= height):
        vel_x = updated_ball.vel.x
        vel_y = updated_ball.vel.y * -1
        vel = Vector(vel_x, vel_y)
        return updated_ball.with_vel(vel)

    return updated_ball
