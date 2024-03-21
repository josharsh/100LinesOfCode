from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
TEAL = "#9FE6A0"
RED = "#F55C47"
GREEN = "#4AA96C"
GREY = "#564A4A"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None
marks = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global marks
    window.after_cancel(time)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", fg=TEAL)
    marks = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_sec)
        timer.config(text="Relax..Take a break for 20 mins ", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_sec)
        timer.config(text="Quick nap for 5 mins?", fg=TEAL)
    else:
        count_down(work_sec)
        timer.config(text="Hustle Hustle for 25 mins!", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global time
    global marks
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{math.floor(count / 60)}:{count_sec}")
    if count > 0:
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREY)

timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=TEAL, bg=GREY)
timer.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 15), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 15), command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(bg=GREY, fg=TEAL, font=(FONT_NAME, 15))
check_label.grid(column=1, row=3)

# Canvas
canvas = Canvas(width=300, height=300, bg=GREY, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 152, image=tomato_img)
timer_text = canvas.create_text(155, 170, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

window.mainloop()
