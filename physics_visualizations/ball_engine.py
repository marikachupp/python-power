from we_made_a_ball import move_ball


# returns instance of Ball
def calculate_new_ball(ball, delta_t_ms):
    delta_t_sec = delta_t_ms / 1000.0
    return move_ball(ball, delta_t_sec)
