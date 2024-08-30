import turtle as t
import random as r

scrn = t.Screen()

running = False

scrn.setup(width=500, height=400)
which_one = scrn.textinput(title="Make a bet", prompt="Which turtle will win the race, Choose a colour")
if which_one:
    running = True

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names_list = ["carl", "cole", "ben", "bob", "rocky", "andy"]
position = [-70, -40, 10, 50, 80, 100]
carls = []

for turty in range(0, 6):
    carl = t.Turtle(shape="turtle")
    carl.penup()
    carl.color(colors[turty])
    carl.goto(x=-230, y=position[turty])
    carls.append(carl)

while running:

    for carl in carls:
        if carl.xcor() > 230:
            running = False
            win = carl.pencolor()
            if carl == which_one:
                print(f"You won! The winning colour is {win}")
            else:
                print(f"You lose! The winning colour is {win}")

        carl.forward(r.randint(0, 15))
scrn.exitonclick()
