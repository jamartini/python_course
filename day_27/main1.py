from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=400, height=300)
window.config(padx=40, pady=30)

# def button_clicked():
#     my_label = Label(text=f"{text_input.get()}", font=("Arial", 20, "bold"))
#     my_label.pack()
#

my_label = Label(text="Label", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)

button = Button(text="BUTTON!")
button.grid(column=1, row=1)

new_button = Button(text=" NEW BUTTON!")
new_button.grid(column=2, row=0)

text_input = Entry(width=10)
text_input.grid(column=3, row=2)

window.mainloop()
