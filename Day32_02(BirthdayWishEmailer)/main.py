import datetime as dt
import pandas
import smtplib
import os
import random

MY_EMAIL = "vibin.smtp.test@gmail.com"
MY_TO_EMAIL = "vibin.smtptest@yahoo.com"
EMAIL_PWD = "***************"
GMAIL_SMTP_SERVER = "smtp.gmail.com"
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

def check_for_birthdays():
    bd_df = pandas.read_csv("birthdays.csv")
    birthdays = bd_df.to_dict(orient="rows")
    # print(birthdays)
    # print(f"Day:{today_day}\tMonth:{today_month}")
    for birthday in birthdays:
        # print(f"Name:{birthday['name']}\tBMonth:{birthday['month']}\tBDay:{birthday['day']}")
        if birthday["month"] == today_month and birthday["day"] == today_day:
            # print(f"Happy Birthday {birthday['name']}")
            send_birthday_wish(birthday['name'], birthday['email'])


def send_birthday_wish(name, email):
    letter = random.choice(os.listdir("./letter_templates"))
    with open(f".\letter_templates\{letter}") as l_file:
        l_content = l_file.read()
        l_content = l_content.replace("[NAME]", name)
    with smtplib.SMTP(GMAIL_SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PWD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday {name}\n\n"
                                f"{l_content}")
        print(f"Sending {name} birthday wishes in email ")


check_for_birthdays()
# letters = os.listdir("./letter_templates")
# print(letters)