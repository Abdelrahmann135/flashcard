from tkinter import *
import pandas
from random import *
BACK_GROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    dic = data.to_dict(orient="records")
else:
    dic = data.to_dict(orient="records")
current = {}


def new_word():
    global current
    current = choice(dic)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current["French"], fill="black")
    canvas.itemconfig(card, image=image1)
    window.after(3000, func=flip_card)
    dic.remove(current)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current["English"], fill="white")
    canvas.itemconfig(card, image=image2)


def save_words():
    df = pandas.DataFrame(dic)
    df.to_csv("data/words_to_learn.csv", index=False)
    new_word()


window = Tk()
window.config(pady=50, padx=50, bg=BACK_GROUND_COLOR)
window.title("Flashy")
canvas = Canvas(width=800, height=526, bg=BACK_GROUND_COLOR, highlightthickness=0)
image1 = PhotoImage(file="E:/pyh/flashcard/images/card_front.png")
image2 = PhotoImage(file="E:/pyh/flashcard/images/card_back.png")
card = canvas.create_image(400, 270, image=image1)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
right_photo = PhotoImage(file="E:/pyh/flashcard/images/right.png")
right_button = Button(image=right_photo, bg=BACK_GROUND_COLOR, highlightthickness=0, borderwidth=0, command=save_words)
right_button.grid(column=1, row=1)
wrong_photo = PhotoImage(file="E:/pyh/flashcard/images/wrong.png")
wrong_button = Button(image=wrong_photo, bg=BACK_GROUND_COLOR, highlightthickness=0, borderwidth=0, command=new_word)
wrong_button.grid(column=0, row=1)
new_word()
window.mainloop()
