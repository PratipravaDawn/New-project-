import turtle as t
from snake import Snake
from score import Scoreboard
from food import Food
import time


def struck_the_x(carl):
    if carl.xcor() > 290 or carl.xcor() < -290:
        return True


def struck_the_y(carl):
    if carl.ycor() > 290 or carl.ycor() < -290:
        return True


scrn = t.Screen()
scrn.setup(width=600, height=600)
scrn.bgcolor("black")
scrn.title("Snake Game")
scrn.tracer(0)

snake = Snake()
apple = Food()
score = Scoreboard()

t.listen()
scrn.onkey(key="s", fun=snake.south)
scrn.onkey(key="w", fun=snake.north)
scrn.onkey(key="a", fun=snake.west)
scrn.onkey(key="d", fun=snake.east)

game = True
while game:
    scrn.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(apple) < 20:
        apple.refresh()
        snake.extend()
        score.points()

    if struck_the_x(snake.head):
        # new_x = snake.head.xcor() * -1
        # snake.head.goto(x=new_x, y=snake.head.ycor())
        snake.reset()
        score.reset()

    if struck_the_y(snake.head):
        # new_y = int(snake.head.ycor()) * -1
        # snake.head.goto(x=snake.head.xcor(), y=new_y)
        snake.reset()
        score.reset()

    for parts in snake.snake[1:]:
        if snake.head.distance(parts) < 10:
            snake.reset()
            score.reset()

scrn.exitonclick()
