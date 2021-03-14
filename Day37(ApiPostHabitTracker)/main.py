import requests
from datetime import datetime

USER_NAME = "vibinvarghese"
TOKEN = "********************"
pixela_endppoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
user_parms = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
response = requests.post(url=pixela_endppoint, json=user_parms)
add_graph_parms = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Kms",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
graph_endpoint = f"{pixela_endppoint}/{USER_NAME}/graphs"
# graph_resp = requests.post(url=graph_endpoint, json=add_graph_parms, headers=headers)
# print(graph_resp.text)

date = datetime(year=2020, month=3, day=17)

post_pixel_data = {
    "date": date.strftime("%Y%m%d"),
    "quantity": "99.3",
}
post_pixel_endpoint = f"{pixela_endppoint}/{USER_NAME}/graphs/{GRAPH_ID}"
# post_pixel_resp = requests.post(url=post_pixel_endpoint, json=post_pixel_data, headers=headers)
# print(post_pixel_resp.text)

date = datetime(year=2020, month=3, day=15)
put_pixel_endpoint = f"{pixela_endppoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
put_pixel_data = {
    "quantity": "0.0"
}
# put_pixel_resp = requests.put(url=put_pixel_endpoint, json=put_pixel_data, headers=headers)
# print(put_pixel_resp.text)

date = datetime(year=2020, month=3, day=15)
del_pixel_endpoint = f"{pixela_endppoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
del_pixel_resp = requests.delete(url=del_pixel_endpoint, headers=headers)