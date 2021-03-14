import requests
from twilio.rest import Client

# Open Weather Map API Details
OWM_URL = "https://api.openweathermap.org/data/2.5/onecall"
KOCHI_LAT = 9.936557
KOCHI_LON = 76.318122
API_KEY = "*****************************"

# Twilio Details
account_sid = "AC*****************************"
auth_token = "*****************************"

client = Client(account_sid, auth_token)

weather_parms = {
    "lat": KOCHI_LAT,
    "lon": KOCHI_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

weather_resp = requests.get(OWM_URL, params=weather_parms)
weather_resp.raise_for_status()
weather_data = weather_resp.json()
it_will_rain = False

for wthr_dt_hour in weather_data["hourly"][0:12]:
    for weather_type in wthr_dt_hour["weather"]:
        print(weather_type["id"])
        if weather_type["id"] < 700:
            it_will_rain = True

if it_will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today buddy. Get an umbrella along. - VB(Dabble-with-Python)",
        from_="+18185321268",
        to="+917907765561"
    )
    print(message.status)
else:
    print("No Rain Forecast for the next 12 hours")
