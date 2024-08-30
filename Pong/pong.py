import turtle as t
from paddle import Paddle, Line
from ball import Ball
from scoreboard import Score
import time

scrn = t.Screen()

scrn.setup(width=800, height=600)
scrn.bgcolor("black")
scrn.title("Pong")

scrn.listen()
scrn.tracer(0)

left_pad = Paddle(xx=-350, yy=0)
right_pad = Paddle(xx=350, yy=0)
ball = Ball()
line = Line()
sc = Score()

scrn.onkeypress(key="w", fun=right_pad.up)
scrn.onkeypress(key="s", fun=right_pad.down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    scrn.update()
    ball.move()
    ball.bounce()
    if ball.distance(right_pad) < 80 and ball.xcor() < 340:
        ball.bounce_pad()
    if ball.xcor() > 400:
        ball.goto(x=0, y=0)
        ball.move_speed = 0.1
        ball.x_move *= -1
        sc.rightscore()

    if ball.xcor() < -400:
        ball.goto(x=0, y=0)
        ball.move_speed = 0.1
        ball.x_move *= -1
        sc.leftscore()


    # while ball.distance(left_pad) > 80 and ball.xcor() > -340:
    #     moves = int(ball.ycor()/30)
    #     if moves > 0:
    #         for x in range(moves):
    #             right_pad.up()
    #     else:
    #         moves *= -1
    #         for x in range(moves):
    #             right_pad.down()




scrn.exitonclick()
