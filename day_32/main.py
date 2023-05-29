import pandas
from smtplib import SMTP
from random import choice
import datetime as dt

MY_EMAIL = "martini.jonatan.a@gmail.com"
PASSWORD = "teovnuweeidygyms"

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict()
birthdays = [f"{data_dict['day'][item]}/{data_dict['month'][item]}" for item in data_dict['day']]
now = dt.datetime.now()
now_date = f"{now.day}/{now.month}"
letter_list = [1, 2, 3]

with SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    for i in range(len(birthdays)):
        if birthdays[i] == now_date:
            letter_index = choice(letter_list)
            letter = f"letter_templates/letter_{letter_index}.txt"
            with open(letter, "r") as file:
                letter_file = file.read()
            letter_file = letter_file.replace('[NAME]', data_dict['name'][i])
            with open(letter, 'w') as file:
                file.write(letter_file)
            with open(letter, 'r') as file:
                msg = file.read()
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Happy Birthday\n\n{msg}"
            )
            letter_original = msg.replace(f"{data_dict['name'][i]}", '[NAME]')
            with open(letter, 'w') as file:
                file.write(letter_original)
