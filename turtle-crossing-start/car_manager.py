from turtle import Turtle
import random as r
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [-250, -230, -210, -190, -170, -150, -130, -110, -90, -70, -50, -30, -10, 0,
         250, 230, 210, 190, 170, 150, 130, 110, 90, 70, 50, 30, 10]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        no = r.randint(1, 6)
        if no == 6:
            c = Turtle("square")
            c.color(r.choice(COLORS))
            c.penup()
            c.shapesize(stretch_wid=1, stretch_len=2)
            yco = r.randint(-250, 250)
            c.goto(x=300, y=yco)
            self.cars.append(c)

    def move(self):
        for c in self.cars:
            c.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
