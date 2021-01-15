import smtplib
import datetime as dt
import random

my_email = "igbxngtest@gmail.com"
password = "abc123"
now = dt.datetime.now()
day_of_the_week = now.weekday()
with open("quotes.txt") as data_file:
    quotes = data_file.readlines()
    quote = random.choice(quotes)

if day_of_the_week == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}".encode("utf-8")
        )

