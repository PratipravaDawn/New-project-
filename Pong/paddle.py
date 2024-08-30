from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xx, yy):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x=xx, y=yy)


    def up(self):
        self.goto(x=self.xcor(), y=self.ycor()+30)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor()-30)


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.goto(x=0, y=300)
        self.pendown()
        self.pensize(width=2)
        self.setheading(270)
        self.hideturtle()
        while self.ycor() != -300:
            self.forward(50)
            self.penup()
            self.forward(50)
            self.pendown()
