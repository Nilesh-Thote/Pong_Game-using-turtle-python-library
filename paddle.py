from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.pad_obj = []
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x, y)

    def mov_up(self):
        if self.ycor() < 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def mov_dowm(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
