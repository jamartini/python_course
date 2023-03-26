from tkinter import *


def convert():
    miles = float(miles_entry.get())
    result = round(miles * 16 / 10)
    km_num_label.config(text=f"{result}")


window = Tk()
window.title("Convert miles to kilometers")
window.minsize(width=200, height=150)
window.config(padx=40, pady=30)

miles_entry = Entry(justify=CENTER)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="miles", font=("Arial", 11, "normal"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 11, "normal"))
equal_label.grid(column=0, row=1)

km_num_label = Label(text="0", font=("Arial", 11, "normal"))
km_num_label.grid(column=1, row=1)

km_label = Label(text="km", font=("Arial", 11, "normal"))
km_label.grid(column=2, row=1)

calc_button = Button(text="CALCULATE", command=convert)
calc_button.grid(column=1, row=2)

window.mainloop()
