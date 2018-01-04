from Tkinter import *

from ball_engine import calculate_new_ball, initialize_ball

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500


class BallFrame:
    def __init__(self, tk, ball):
        self.tk = tk
        self.ball = ball
        self.canvas = Canvas(tk, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="grey")
        self.canvas.pack()

        ball_diameter = 2 * ball.rad
        self.oval_view = self.canvas.create_oval(0, 0, ball_diameter, ball_diameter, fill='black')
        self.update_loop()

    def update_loop(self):
        delta_t_ms = 16

        updated_ball = calculate_new_ball(self.ball, delta_t_ms, WINDOW_WIDTH, WINDOW_HEIGHT)
        delta_x = updated_ball.pos.x - self.ball.pos.x
        delta_y = updated_ball.pos.y - self.ball.pos.y

        self.canvas.move(self.oval_view, delta_x, delta_y)

        self.ball = updated_ball

        self.tk.after(delta_t_ms, self.update_loop)

    def main_loop(self):
        self.tk.mainloop()


bouncy = initialize_ball()

ballFrame = BallFrame(Tk(), bouncy)
ballFrame.main_loop()
