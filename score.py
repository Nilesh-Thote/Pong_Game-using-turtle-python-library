from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.lscore = 0
        self.rscore = 0
        self.penup()
        self.goto(x=0, y=-300)
        self.pendown()
        self.left(90)
        self.pensize(width=3)
        self.draw()
        self.hideturtle()
        self.updatescore()

    def draw(self):
        while self.ycor() < 300:
            self.fd(10)
            self.penup()
            self.goto(x=0, y=self.ycor() + 10)
            self.pendown()

    def updatescore(self):
        self.clear()
        self.penup()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Arial", 80, "normal"))

    def lpoint(self):
        self.lscore += 1
        self.updatescore()

    def rpoint(self):
        self.rscore += 1
        self.updatescore()

    def winl(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"Player1 win with score of {self.lscore}", align="center", font=("Arial", 20, "normal"))

    def winr(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"Player2 win with score of {self.rscore}", align="center", font=("Arial", 20, "normal"))
