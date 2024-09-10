from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flash Cards')

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

bg_img = PhotoImage(file='images/card_back.png')
canvas.create_image(400, 263, image=bg_img)
fg_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=fg_img)
canvas.grid(column=0, columnspan=2, row=0)

wrong_img = PhotoImage(file='images/wrong.png')
canvas.create_image(canvas.winfo_width()/2, canvas.winfo_height()/2, image=wrong_img)
canvas.grid(column=0, row=1)




window.mainloop()
