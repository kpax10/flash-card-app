import csv
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def remove_word():
    if current_card in to_learn_list:
        to_learn_list.remove(current_card)
        print(f'{current_card} removed')
        print(len(to_learn_list))

        with open('data/words_to_learn.csv', 'w', newline='') as file:
            header = to_learn_list[0].keys()
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(to_learn_list)
    next_card()


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn_list)
    canvas.itemconfig(card_title, text="Italian", fill='black')
    canvas.itemconfig(card_word, text=current_card['Italian'], fill='black')
    canvas.itemconfig(canvas_image, image=card_front_img)
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, fill='white')
    canvas.itemconfig(card_title, text='English')
    canvas.itemconfig(card_word, fill='white')
    canvas.itemconfig(card_word, text=current_card['English'])


try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/italian_words.csv')
finally:
    to_learn_list = df.to_dict(orient='records')

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flash Cards')
timer = window.after(3000, flip_card)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Language", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="word", font=('Ariel', 60, 'bold'))
canvas.grid(column=0, columnspan=2, row=0)

unknown_img = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=unknown_img, borderwidth=0, relief='flat', bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(column=0, row=1)
known_img = PhotoImage(file='images/right.png')
known_button = Button(image=known_img, borderwidth=0, relief='flat', bg=BACKGROUND_COLOR, command=remove_word)
known_button.grid(column=1, row=1)

next_card()


window.mainloop()
