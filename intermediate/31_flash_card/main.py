from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_word = {}
try:
    data_csv = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data_csv = pd.read_csv("data/french_words.csv")
    to_learn = original_data_csv.to_dict(orient='records')
else:
    to_learn = data_csv.to_dict(orient='records')

# -------------------  CHANGE WORDS  -------------------#
def change_word():
    global current_word, flip_timer
    screen.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(bg, image=flash_card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f'{current_word["French"]}', fill="black")
    flip_timer = screen.after(3000, func=flip_card)
def flip_card():
    global current_word
    canvas.itemconfig(bg, image=flash_card_back)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=f'{current_word["English"]}')

def is_known():
    to_learn.remove(current_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_word()

# -------------------  UI  -------------------#
screen = Tk()
screen.title("Flash card")
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer =screen.after(3000, func=flip_card)
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front = PhotoImage(file="images/card_front.png")
flash_card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
bg = canvas.create_image(400, 275, image=flash_card_front)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_btn = Button(image=wrong, highlightthickness=0, highlightbackground=BACKGROUND_COLOR
                   , highlightcolor=BACKGROUND_COLOR, command=change_word)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right, highlightthickness=0, highlightbackground=BACKGROUND_COLOR
                   , highlightcolor=BACKGROUND_COLOR, command=is_known)
right_btn.grid(column=1, row=1)

screen.mainloop()