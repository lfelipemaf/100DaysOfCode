import requests
import os
from datetime import datetime

APP_ID = "222af488"
API_KEY = os.environ.get("NUTRTIONIX_API_KEY")

nutrtionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/cda7d577640637682066412616bda557/myWorkouts/workouts"


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
activity = input("Tell me which exercise you did: ")
data = {
    "query": activity,
    "gender": "male",
    "weight_kg": 105.0,
    "height_cm": 175.00,
    "age": 30
}

response = requests.post(url=nutrtionix_endpoint,headers=headers,json=data,verify=False)
req = response.json()
exercises = req['exercises']

today = datetime.now()

for exercise in exercises:
    log_data = {
        "workout": {
                "date": today.strftime("%d/%m/%Y"),
                "time": today.strftime("%H:%I:%S"),
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
    }
    response = requests.post(url=sheety_endpoint,verify=False,json=log_data)

response = requests.get(url=sheety_endpoint,verify=False)
print(response.text)

