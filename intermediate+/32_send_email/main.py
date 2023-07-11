import smtplib
import creds

my_email = creds.cred["user"]
password = creds.cred["password"]

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="lfelipemaf@icloud.com",
                        msg="Subject:Hello\n\nThis is the body of the mail")
