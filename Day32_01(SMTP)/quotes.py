import datetime as dt
import random
import smtplib

MY_EMAIL = "vibin.smtp.test@gmail.com"
MY_TO_EMAIL = "vibin.smtptest@yahoo.com"
EMAIL_PWD = "***************"
GMAIL_SMTP_SERVER = "smtp.gmail.com"

with open("quotes.txt", mode="r") as q_file:
    quotes = [quote.rstrip("\n") for quote in q_file.readlines()]
    # print(quotes)

with smtplib.SMTP(GMAIL_SMTP_SERVER) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=EMAIL_PWD)
    today_day_of_week = dt.datetime.now().weekday()
    if today_day_of_week == 3:
        quote_for_today = random.choice(quotes)
        print(f"Quote for the Day:\n{quote_for_today}")
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_TO_EMAIL,
                            msg=f"Subject:Monday Motivator\n\n"
                                f"{quote_for_today}")



