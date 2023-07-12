import smtplib
import creds
import datetime as dt
import random
import pandas as pd

PLACEHOLDER = "[NAME]"

my_email = creds.cred["user"]
password = creds.cred["password"]

cur_date = dt.datetime.now()

birthdays = pd.read_csv("birthdays.csv")
receiver = birthdays[birthdays.month == cur_date.month][birthdays.day == cur_date.day]
receiver_dict = receiver.to_dict()

person = receiver_dict['name'][0]
receiver_email = receiver_dict['email'][0]

with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as messages:
    list_of_messages = messages.read()
    new_letter = list_of_messages.replace(PLACEHOLDER, person)


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email,
                            msg=f"Subject:Happy birthday\n\n{new_letter}")




