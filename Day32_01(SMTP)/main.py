import smtplib

my_email = "vibin.smtp.test@gmail.com"
email_password = "***************"
GMAIL_SMTP_SERVER = "smtp.gmail.com"

with smtplib.SMTP(GMAIL_SMTP_SERVER) as connection:
    connection.starttls()
    connection.login(user=my_email, password=email_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="vibin.smtptest@yahoo.com",
                        msg="subject:Hello\n\n"
                            "Hi! This is automated email from Python smtplib")
# connection.close()