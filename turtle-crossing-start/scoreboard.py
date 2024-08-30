from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 0
        self.penup()
        self.hideturtle()
        self.goto(x=-250, y=250)
        self.write(f"Level : {self.lvl}", font=FONT)

    def increase_lbl(self):
        self.clear()
        self.lvl += 1
        self.write(f"Level : {self.lvl}", font=FONT)

    def gameover(self):
        self.clear()
        self.goto(x=-200, y=0)
        self.write("GAME OVER", font=("Courier", 50, "normal"))
