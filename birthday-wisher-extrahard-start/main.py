##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "igbxngtest@gmail.com"
password = "abc123"

# 1. Update the birthdays.csv
with open("birthdays.csv", "a") as data_file:
    new_birthday = "Tom,tom@gmail.com,1996,03,14"
    data_file.write(f"\n{new_birthday}")

# 2. Check if today matches a birthday in the birthdays.csv
df = pd.read_csv("birthdays.csv")
birthdays = [dt.datetime(year, month, day) for year, month, day in zip(df['year'], df['month'], df['day'])]
for index, bday in zip(range(len(birthdays)), birthdays):
    if bday.date().day == dt.datetime.today().day and bday.date().month == dt.datetime.today().month:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        letter_index = random.choice(range(1, 4))
        recipient = df.iloc[index]
        with open(f"letter_templates/letter_{letter_index}.txt") as temp_letter:
            temp_letter = temp_letter.read()
            letter = temp_letter.replace("[NAME]", recipient['name'])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient['email'],
                msg=f"Subject:Happy Birthday\n\n{letter}"
            )



