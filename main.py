from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flash Cards')
window.resizable(False, False)

card_canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_img = PhotoImage(file='images/card_back.png')
card_canvas.create_image(400, 263, image=bg_img)
fg_img = PhotoImage(file='images/card_front.png')
card_canvas.create_image(400, 263, image=fg_img)
card_canvas.grid(column=0, columnspan=2, row=0)

language_label = Label(window, text='Language', font=('Ariel', 40, 'italic'), bg='white')
language_label.place(x=400, y=150, anchor='center')

word_label = Label(text='word', font=('Ariel', 60, 'bold'), bg='white', anchor='center')
word_label.place(x=400, y=263, anchor='center')

wrong_canvas = Canvas(window, width=99, height=99, highlightthickness=0)
wrong_img = PhotoImage(file='images/wrong.png')
wrong_canvas.create_image(49, 49, image=wrong_img)
wrong_canvas.grid(column=0, row=1)

correct_canvas = Canvas(window, width=100, height=100, highlightthickness=0)
correct_img = PhotoImage(file='images/right.png')
correct_canvas.create_image(50, 50, image=correct_img)
correct_canvas.grid(column=1, row=1)






window.mainloop()
