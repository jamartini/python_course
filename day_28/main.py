from tkinter import *
from math import floor
import pygame

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

pygame.mixer.init()

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(fg=GREEN, text="TIMER", bg=YELLOW, font=(FONT_NAME, 26, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0


def count_down(time):
    count_min = floor(time / 60)
    count_sec = time % 60
    if count_sec < 10:
        canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
    else:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if time > 0:
        global timer
        timer = window.after(1000, count_down, time - 1)
    else:
        marks = ""
        sessions = floor(reps/2)
        for i in range(sessions):
            marks += "✔"
        checkmarks.config(text=marks)
        start_timer()


def start_timer():
    global reps
    reps += 1
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        title_label.config(text="WORK", fg=GREEN)
        pygame.mixer.music.load("work.wav")
        pygame.mixer.music.play(loops=0)
        count_down(WORK_MIN * 60)
    elif reps == 2 or reps == 4 or reps == 6:
        title_label.config(text="BREAK", fg=PINK)
        pygame.mixer.music.load("break.wav")
        pygame.mixer.music.play(loops=0)
        count_down(SHORT_BREAK_MIN * 60)
    elif reps == 8:
        title_label.config(text="BREAK", fg=RED)
        pygame.mixer.music.load("break.wav")
        pygame.mixer.music.play(loops=0)
        count_down(LONG_BREAK_MIN * 60)


start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

checkmarks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "normal"))
checkmarks.grid(column=1, row=3)

window.mainloop()
