from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.y = 10
        self.x = 10
        self.ball_speed = 0.1

    def move(self):
        xnew = self.xcor() + self.x
        ynew = self.ycor() + self.y
        self.penup()
        self.goto(xnew, ynew)

    def bounce_wall(self):
        self.y *= -1

    def bounce_paddle(self):
        self.x *= -1
        self.ball_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_paddle()
