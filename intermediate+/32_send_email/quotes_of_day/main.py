import smtplib
import creds
import datetime as dt
import random


my_email = creds.cred["user"]
password = creds.cred["password"]

with open("quotes.txt") as messages:
    list_of_messages = messages.readlines()
    message_of_day = random.choice(list_of_messages)

print(message_of_day)

if dt.datetime.now().weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="lfelipemaf@icloud.com",
                            msg=f"Subject:Motivation\n\n{message_of_day}")




