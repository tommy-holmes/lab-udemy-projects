from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
random_index = None
try:
    with open("data/words_to_learn.csv", "r") as data_file:
        data = pd.read_csv(data_file)
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

french_to_english_list = data.to_dict(orient="records")


# ---------------------------- TIMER ------------------------------- #
def timer_reset():
    window.after_cancel(timer)


def start_timer():
    global timer
    timer = window.after(3000, show_english_translation)


# ---------------------------- DATA ------------------------------- #
def gen_random_index():
    return random.randint(0, len(french_to_english_list) - 1)


def right_pressed():
    if random_index is not None:
        del french_to_english_list[random_index]
    get_french_word()


def get_french_word():
    global random_index
    random_index = gen_random_index()
    french_word = french_to_english_list[random_index]["French"]
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=french_word)
    start_timer()


def show_english_translation():
    global random_index
    english_word = french_to_english_list[random_index]["English"]
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=english_word)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card Languages")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_img = canvas.create_image(450, 300, image=card_front_img)
title_text = canvas.create_text(450, 175, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(450, 300, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=get_french_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_pressed)
right_button.grid(row=1, column=1)

window.mainloop()

with open("data/words_to_learn.csv", "w") as data_file:
    df = pd.DataFrame(french_to_english_list)
    df.to_csv("data/words_to_learn.csv", index=False)