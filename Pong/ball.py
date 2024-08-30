import turtle as t


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setposition(x=0, y=0)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        if self.ycor() > 280:
            self.y_move = -10
        elif self.ycor() < -280:
            self.y_move = 10

    def bounce_pad(self):
        self.x_move *= -1
        self.move_speed *= 0.5
