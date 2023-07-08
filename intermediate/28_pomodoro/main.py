from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    global reps
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    checks.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 0

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)

def count_down(count):
    global timer
    minutes = math.floor(count/60)
    if minutes < 10:
        minutes = f'0{minutes}'
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        checks.config(text=mark)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title.grid(column=1, row=0)
start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
checks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
checks.grid(column=1, row=3)
window.mainloop()
