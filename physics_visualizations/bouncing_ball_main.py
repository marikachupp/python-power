from Tkinter import *

from ball_engine import calculate_new_ball
from learning_vectors import Vector
from we_made_a_ball import Ball

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
BALL_RADIUS = 50


class BallFrame:
    def __init__(self, tk, ball):
        self.tk = tk
        self.ball = ball
        self.canvas = Canvas(tk, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack()

        self.oval_view = self.canvas.create_oval(0, 0, BALL_RADIUS, BALL_RADIUS, fill='black')
        self.update_loop()

    def update_loop(self):
        delta_t_ms = 16

        updated_ball = calculate_new_ball(self.ball, delta_t_ms)
        delta_x = updated_ball.pos.x - self.ball.pos.x
        delta_y = updated_ball.pos.y - self.ball.pos.y

        self.canvas.move(self.oval_view, delta_x, delta_y)

        self.ball = updated_ball

        self.tk.after(delta_t_ms, self.update_loop)

    def main_loop(self):
        self.tk.mainloop()


bouncy = Ball(pos=Vector(0, 0), vel=Vector(20, 18))

ballFrame = BallFrame(Tk(), bouncy)
ballFrame.main_loop()
