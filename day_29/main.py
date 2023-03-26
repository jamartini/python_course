from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("Arial", 9, "normal")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_lb = Label(text="Website:", font=FONT)
website_lb.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky='EW')
website_entry.focus()


def search():
    try:
        with open("data.json", "r") as df:
            data = json.load(df)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There's no such file.")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="File is empty.")
    else:
        if len(website_entry.get()) == 0:
            messagebox.showinfo(title="Error", message="Field was left empty.")
        else:
            if website_entry.get() in data:
                website = website_entry.get()
                user = data[f"{website}"]["email"]
                password = data[f"{website}"]["password"]
                data_message = f"Email: {user}\nPassword: {password}"
                messagebox.showinfo(title="Website found", message=data_message)
            else:
                messagebox.showinfo(title="Website not found", message="Website not found")


search_button = Button(width=14, text='Search', padx=0, pady=0, font=FONT, command=search)
search_button.grid(column=2, row=1, sticky='EW')

user_lb = Label(text="Email/Username:", font=FONT)
user_lb.grid(column=0, row=2)

user_entry = Entry(width=35)
user_entry.insert(0, "email@email.com")
user_entry.grid(column=1, row=2, columnspan=2, sticky='EW')

pw_label = Label(text="Password:", font=FONT)
pw_label.grid(column=0, row=3)

pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3, sticky='EW')


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for _ in range(nr_letters)]
    password_list.extend([choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([choice(numbers) for _ in range(nr_numbers)])

    shuffle(password_list)

    password = "".join(password_list)
    pw_entry.insert(0, password)
    pyperclip.copy(password)


generate_pw = Button(text='Generate', width=14, padx=0, pady=0, font=FONT, command=generate_password)
generate_pw.grid(column=2, row=3, sticky='EW')


def add_function():
    if len(website_entry.get()) == 0 or len(pw_entry.get()) == 0:
        messagebox.showerror(title="Error", message="Don't leave any fields empty!")

    else:
        website = website_entry.get()
        user = user_entry.get()
        password = pw_entry.get()
        new_data = {
            website: {
                "email": user,
                "password": password,
            }
        }
        try:
            with open("data.json", "r") as df:
                data = json.load(df)
                data.update(new_data)
            with open("data.json", "w") as df:
                json.dump(data, df, indent=4)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as df:
                json.dump(new_data, df, indent=4)
        finally:
            website_entry.delete(0, END)
            pw_entry.delete(0, END)
            website_entry.focus()


add = Button(width=36, text='Add', padx=0, pady=0, font=FONT, command=add_function)
add.grid(column=1, row=4, columnspan=2, sticky='EW')

window.mainloop()
