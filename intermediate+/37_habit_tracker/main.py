import requests
from datetime import datetime

USERNAME = "lfelipemaf"
TOKEN = "An76jf4823h23ns9d"

pixela_endpoint = f"https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=params, verify=False)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Days going to GYM",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers, verify=False)
# print(response.text)

today = datetime.now()
print(today.strftime("%Y%m%d"))

graph1_endpoint = f"{graph_endpoint}/graph1"
data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

response = requests.post(url=graph1_endpoint, headers=headers, json=data, verify=False)
print(response.text)