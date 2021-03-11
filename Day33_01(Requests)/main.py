import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response = requests.get(url="http://api.open-notify.org/iss-now.json1")
print(response)
print(response.status_code)
response.raise_for_status()

resp_data = response.json()
print(resp_data["iss_position"])

iss_position = (resp_data["iss_position"]["latitude"], resp_data["iss_position"]["longitude"])
print(iss_position)





