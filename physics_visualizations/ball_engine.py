from learning_vectors import Vector
from we_made_a_ball import move_ball, Ball

BALL_RADIUS = 50


def initialize_ball():
    return Ball(pos=Vector(0, 0), vel=Vector(100, 60), rad=BALL_RADIUS)


# returns instance of Ball
def calculate_new_ball(ball, delta_t_ms, width, height):
    delta_t_sec = delta_t_ms / 1000.0

    updated_ball = move_ball(ball, delta_t_sec)
    new_pos_x = updated_ball.pos.x
    new_pos_y = updated_ball.pos.y

    diameter = (2 * ball.rad)
    print new_pos_x, new_pos_y, diameter

    if (0 <= new_pos_y) and (new_pos_y + diameter <= height) \
            and (0 <= new_pos_x) and (new_pos_x + diameter <= width):
        return updated_ball
    else:
        return ball
