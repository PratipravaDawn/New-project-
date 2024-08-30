import turtle as t

INITIALS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.move()

    def create_snake(self):
        for pos in INITIALS:
            self.add_body(pos)

    def add_body(self, pos):
        body = t.Turtle()
        body.color("green")
        body.shape("square")
        body.penup()
        body.goto(pos)
        self.snake.append(body)

    def reset(self):
        for s in self.snake:
            s.goto(x=1000, y=1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        self.add_body(self.snake[-1].position())

    def move(self):
        for segno in range(len(self.snake) - 1, 0, -1):
            x = self.snake[segno - 1].xcor()
            y = self.snake[segno - 1].ycor()
            self.snake[segno].goto(x, y)
        self.head.forward(DISTANCE)

    def north(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def east(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def south(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
