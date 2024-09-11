from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"



window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flash Cards')
window.resizable(False, False)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Language", font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text="word", font=('Ariel', 60, 'bold'))
canvas.grid(column=0, columnspan=2, row=0)

unknown_img = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=unknown_img, borderwidth=0, relief='flat', bg=BACKGROUND_COLOR)
unknown_button.grid(column=0, row=1)
known_img = PhotoImage(file='images/right.png')
known_button = Button(image=known_img, borderwidth=0, relief='flat', bg=BACKGROUND_COLOR)
known_button.grid(column=1, row=1)


window.mainloop()
