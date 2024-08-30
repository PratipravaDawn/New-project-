import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
game_is_on = False
c = (screen.textinput(title="Turtle Crossing", prompt="Start:")).lower()
if c == "start":
    game_is_on = True
screen.listen()
screen.tracer(0)

titty = Player()
obs = CarManager()
level = Scoreboard()

screen.onkey(fun=titty.move, key="w")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    obs.create_car()
    obs.move()
    for c in obs.cars:
        if titty.distance(c) <= 20:
            level.gameover()
            game_is_on = False

    if titty.finishes():
        level.increase_lbl()
        obs.increase_speed()

screen.exitonclick()
