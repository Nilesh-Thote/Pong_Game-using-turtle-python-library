""" 2 players can play this game
    player1 can use 'w' and 's' key to move
    player2 can use arrow key to move
    """
from turtle import Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.tracer(0)
paddle_right = Paddle(x=350, y=0)
paddle_left = Paddle(x=-350, y=0)
ball = Ball()
score = Score()
s.update()
s.listen()
s.onkeypress(paddle_right.mov_up, "Up")
s.onkeypress(paddle_right.mov_dowm, "Down")
s.onkeypress(paddle_left.mov_up, "w")
s.onkeypress(paddle_left.mov_dowm, "s")
gameison = True
while gameison:
    s.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # detection of collision with walls to bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # detection of collision with paddle to bounce back
    if ball.distance(paddle_right) < 55 and ball.xcor() > 340 or ball.distance(paddle_left) < 55 and ball.xcor() < -340:
        ball.bounce_paddle()

    # detection of collision with wall positive x axis
    if ball.xcor() > 380:
        score.rpoint()
        ball.ball_reset()

    # detection of collision with wall negative x axis
    if ball.xcor() < -380:
        score.lpoint()
        ball.ball_reset()

    if score.lscore == 3:
        score.winl()
        gameison = False
    if score.rscore == 3:
        score.winr()
        gameison = False

s.exitonclick()
