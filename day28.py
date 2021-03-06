#!/usr/bin env python3
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pamodoro")
window.minsize(width = 200, height = 200)
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 220, bg = YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file = "/home/logan/VS Code Projects/Python/100 Days coding/day28/tomato.png")
canvas.create_image(100,109, image = tomato_image)
canvas.create_text(101, 130, text = "00:00",fill = 'white', font = ("Courier", 35, "bold"))

canvas.pack()


window.mainloop()