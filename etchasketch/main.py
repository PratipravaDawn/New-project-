import turtle as t

carl = t.Turtle()
scrn = t.Screen()

carl.pensize(5)


def forward():
    carl.forward(10)


def backward():
    carl.back(10)


def anti():
    carl.left(30)


def clock():
    carl.right(30)


i = 0
p = 1


def color():
    c = ['red', 'blue', 'green', 'black']
    global i
    ink = c[i]
    i += 1
    if i > 3:
        i = 0
    return carl.color(ink)


def erase():
    carl.pencolor("white")


def clear():
    carl.clear()
    carl.penup()
    carl.home()
    carl.pendown()


# def increse_pen():
#     global p
#     carl.pensize(p + 2)
#
#
# def decrese_pen():
#     global p
#     carl.pensize(p - 2)


scrn.onkeypress(key='w', fun=forward)
scrn.onkeypress(key='s', fun=backward)
scrn.onkeypress(key='a', fun=anti)
scrn.onkeypress(key='d', fun=clock)
scrn.onkey(key='space', fun=color)
scrn.onkey(key='c', fun=clear)
scrn.onkey(key='e', fun=erase)
# scrn.onkey(key='p', fun=increse_pen)
# scrn.onkey(key='o', fun=decrese_pen)

scrn.listen()
scrn.exitonclick()
