import datetime as dt
from random import choice
from smtplib import SMTP

MY_EMAIL = "martini.jonatan.a@gmail.com"
PASSWORD = "teovnuweeidygyms"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        chosen_quote = choice(quotes)
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Monday Motivation\n\n{chosen_quote}"
            )
