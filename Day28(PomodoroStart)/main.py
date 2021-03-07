from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
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

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_secs = 60 * WORK_MIN
    short_break_secs = 60 * SHORT_BREAK_MIN
    long_break_secs = 60 * LONG_BREAK_MIN
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_secs)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_secs)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count_in_secs):
    count_mins = math.floor(count_in_secs / 60)
    count_secs = count_in_secs % 60
    canvas.itemconfig(timer_text, text=f"{count_mins:02}:{count_secs:02}")
    if count_in_secs > 0:
        global timer
        timer = window.after(1000, count_down, count_in_secs-1)
    else:
        start_timer()
        marks=""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # highlight thickness=0 to remove the img brdr
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



# Timer Title
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)



# Start Button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

# CheckMark
check_mark = "✅"
check_marks = Label(text=check_mark, fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)



window.mainloop()
