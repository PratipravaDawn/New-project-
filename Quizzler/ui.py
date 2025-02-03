from  tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self, qizzy:QuizBrain):
        self.quiz = qizzy

        self.scrn = Tk()
        self.scrn.title("Quizz Machine")
        self.scrn.minsize(width=250, height=500)
        self.scrn.config(bg=THEME_COLOR)

        self.lable = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.lable.grid_configure(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 125,
                                            text="TEXT IS HERE",
                                            fill=THEME_COLOR,
                                            font=("Arial", 20, "italic"),
                                            width=280)
        self.canvas.grid_configure(row=1, column=0, columnspan=2, padx=20, pady=20)

        YESSS = PhotoImage(file="images/true.png")
        NOOO = PhotoImage(file="images/false.png")
        self.yes = Button(image=YESSS, command=self.right_button)
        self.yes.grid_configure(row=2, column=1, pady= 20, padx=20)
        self.no = Button(image=NOOO, command=self.wrong_button)
        self.no.grid_configure(row=2, column=0, padx=20, pady=20)

        self.next_question()
        self.scrn.mainloop()

    def change_score(self):
        self.lable.config(text=f"Score: {self.quiz.score}")

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=question)
        else:
            self.canvas.itemconfig(self.text, text="GG<3 QUIZ HAS ENDED")
            self.yes.config(state="disabled")
            self.no.config(state="disabled")


    def right_button(self):
        if self.quiz.check_answer("True"):
            self.change_score()
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.scrn.after(1000, self.next_question)

    def wrong_button(self):
        if self.quiz.check_answer("False"):
            self.change_score()
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.scrn.after(1000, self.next_question)






