import requests
from datetime import datetime
import smtplib

ISS_API_URL = "http://api.open-notify.org/iss-now.json"
SUN_API_URL = "https://api.sunrise-sunset.org/json"
MY_LAT = 10.057906
MY_LNG = 76.346359
POS_TOLERANCE = 250
MY_EMAIL = "vibin.smtp.test@gmail.com"
MY_TO_EMAIL = "vibin.smtptest@yahoo.com"
EMAIL_PWD = "**********"
GMAIL_SMTP_SERVER = "smtp.gmail.com"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


def get_iss_pos():
    iss_resp = requests.get(url=ISS_API_URL)
    iss_resp.raise_for_status()
    iss_resp_data = iss_resp.json()
    iss_pos_lat = int(iss_resp_data["iss_position"]["latitude"].split('.')[0])
    iss_pos_lng = int(iss_resp_data["iss_position"]["longitude"].split('.')[0])
    return iss_pos_lat, iss_pos_lng


def is_iss_near(iss_pos_lcl):
    if ((iss_pos_lcl[0] - MY_LAT) ** 2 < POS_TOLERANCE ** 2) and ((iss_pos_lcl[1] - MY_LNG) ** 2 < POS_TOLERANCE ** 2):
        return True
    else:
        return False


def is_it_dark():
    sun_resp = requests.get(SUN_API_URL, params=parameters)
    sun_resp.raise_for_status()
    data = sun_resp.json()
    sunrise_time = data["results"]["sunrise"]
    sunset_time = data["results"]["sunset"]
    print(f"Sunrise at:{sunrise_time}\tSunset at:{sunset_time}")

    sunrise_hr = int(sunrise_time.split('T')[1].split(':')[0])
    sunset_hr = int(sunset_time.split('T')[1].split(':')[0])
    print(f"Sunrise at:{sunrise_hr}\tSunset at:{sunset_hr}")

    hour_now = datetime.utcnow().hour
    if (hour_now >= sunrise_hr) and (hour_now < sunset_hr):
        return False
    else:
        return True


def send_email():
    with smtplib.SMTP(GMAIL_SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PWD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Look Up!\n\n"
                                f"Look Up Now to spot the ISS!")


iss_pos = get_iss_pos()
print(iss_pos)
if is_iss_near(iss_pos) and is_it_dark():
    send_email()
    print("Email sent")
