from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#29C753"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 1
time = None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global time
    global rep
    rep = 1
    screen.after_cancel(time)
    text_front.config(text="Timer", fg= GREEN)
    paper.itemconfig(timer, text="00:00")
    check.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    work_sec = WORK_MIN*60
    sbreak_sec = SHORT_BREAK_MIN*60
    lbreak_sec = LONG_BREAK_MIN*60
    if rep % 2 != 0 and rep < 8:
        countdown(work_sec)
        rep += 1
        text_front.config(text="WORK", fg=PINK)
    elif rep < 8:
        countdown(sbreak_sec)
        rep += 1
        text_front.config(text="BREAK", fg=RED)
    else:
        countdown(lbreak_sec)
        text_front.config(text="LONG BREAK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minute = math.floor(count / 60)
    if minute < 10:
        minute = f"0{minute}"
    seconds = int(count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    paper.itemconfig(timer, text=f"{minute}:{seconds}")
    if count > 0:
        global time
        time = screen.after(1000, countdown, count-1)
    else:
        start_timer()
        if rep == 1:
            check.config(text="✔")
        if rep == 3:
            check.config(text="✔✔")
        if rep == 5:
            check.config(text="✔✔✔")
# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("POMODORO")
screen.config(pady=100, padx=100, bg=YELLOW)

text_front = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg= YELLOW)
text_front.grid_configure(row=0, column=1)
paper = Canvas(height=240, width=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
paper.create_image(100, 110, image= img)
timer = paper.create_text(100, 140, fill="white", text="00:00", font=(FONT_NAME, 35, "bold"))
paper.grid_configure(row=1, column=1)

start_button = Button(text="START", bg=GREEN, fg="white", command=start_timer)
start_button.grid_configure(row=2, column=0)

check = Label(text="", fg=GREEN, bg=YELLOW, font=(40))
check.grid_configure(row=2, column=1)

reset = Button(text="RESET", bg=RED, fg="white", command=timer_reset)
reset.grid_configure(row=2, column=2)





screen.mainloop()