from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

words_df = pandas.read_csv("it_en_test.csv")
words_dict = words_df.to_dict(orient="records")
index = randint(0, len(words_dict)-1)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = card.create_image(400, 263, image=front_img)
lng_text = card.create_text(400, 150, text="Italian", font=LANGUAGE_FONT)
word_text = card.create_text(400, 263, text=f"{words_dict[index]['Italian'].upper()}", font=WORD_FONT)
card.grid(column=0, row=0, columnspan=2)
gone_indexes = []


def flip_card():
    global index
    card.itemconfig(card_img, image=back_img)
    card.itemconfig(lng_text, text="English", fill="white")
    card.itemconfig(word_text, text=f"{words_dict[index]['English'].upper()}", fill="white")


def change_word():
    global index, words_dict, flip, gone_indexes
    window.after_cancel(flip)
    if len(words_dict) == 0:
        pass
    elif len(words_dict) == 1:
        index = 0
    else:
        index = randint(0, len(words_dict)-1)
        if index in gone_indexes:
            while index in gone_indexes:
                index = randint(0, len(words_dict) - 1)
        card.itemconfig(card_img, image=front_img)
        card.itemconfig(lng_text, text="Italian", fill="black")
        card.itemconfig(word_text, text=f"{words_dict[index]['Italian'].upper()}", fill="black")


def only_change():
    global flip
    change_word()
    flip = window.after(3000, flip_card)


def remove_word():
    if len(words_dict) <= 1:
        pass
    else:
        try:
            global index
            words_dict.remove(words_dict[index])
        except IndexError:
            pass


def change_and_remove():
    global flip, gone_indexes
    gone_indexes.append(index)
    change_word()
    remove_word()
    flip = window.after(3000, flip_card)


flip = window.after(3000, func=flip_card)

known_img = PhotoImage(file="images/right.png")
known = Button(image=known_img, highlightthickness=0, command=change_and_remove)
known.grid(column=0, row=1)

unknown_img = PhotoImage(file="images/wrong.png")
unknown = Button(image=unknown_img, highlightthickness=0, command=change_word)
unknown.grid(column=1, row=1)


window.mainloop()
