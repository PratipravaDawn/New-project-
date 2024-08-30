from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.sc = 0
        with open("highscore.txt", mode="r") as file:
            self.hs = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write(align="center", arg="Game Over", font=("Times New Roman", 30, "normal"))

    def update_score(self):
        self.clear()
        self.write(align="center", arg=f"Score = {self.sc} Highscore = {self.hs}", font=("Times New Roman", 15, "normal"))

    def points(self):
        self.sc += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.sc > self.hs:
            self.hs = self.sc
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.hs}")
        self.sc = 0
        self.update_score()
