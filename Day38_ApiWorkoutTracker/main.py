import requests
import datetime
import os

# Nutritionix API Details
APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ.get("NT_API_KEY")

print(f"APP_ID:{APP_ID}")
GENDER = "male"
WEIGHT_KG = 89.9
HEIGHT_CM = 178.2
AGE = 36
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

user_query = input("Tell me the exercises you did today:")
exercise_params = {
    "query": user_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_resp = requests.post(url=exercise_endpoint, headers=headers, json=exercise_params)
exercise_resp.raise_for_status()
exercise_list = exercise_resp.json()["exercises"]

now = datetime.datetime.now()
date_now = now.strftime("%d/%m/%Y")
time_now = now.strftime("%H:%M:%S")

# Sheet Update API Details
SHEET_ENDPOINT = "https://api.sheety.co/9cbbfd5fb78ba1c880bee3c677110bf8/myWorkouts/workouts"
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")
sheet_headers = {
    "Authorization": "Bearer " + SHEET_TOKEN
}

for ex_item in exercise_list:
    sheet_log_data = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": ex_item["name"].title(),
            "duration": float(ex_item["duration_min"]),
            "calories": float(ex_item["nf_calories"]),
        }
    }
    print(f"Ex Item:\n{ex_item}")
    sheet_update_resp = requests.post(url=SHEET_ENDPOINT, headers=sheet_headers, json=sheet_log_data)
    print(sheet_update_resp.text)


sheet_get_resp = requests.get(url=SHEET_ENDPOINT, headers=sheet_headers)
print(sheet_get_resp.json())
