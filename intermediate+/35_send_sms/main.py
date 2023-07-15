from creds import api_key
import requests

MY_LAT = -20.316839
MY_LONG = -40.309921

weather_endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={MY_LAT}&lon={MY_LONG}&appid={api_key}&units=metric"

response = requests.get(url=weather_endpoint, verify=False)
response.raise_for_status()
data = response.json()

weather_img = f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
cur_weather = data["weather"][0]["description"]

cur_temp = data["main"]["temp"]
cur_feels_like = data["main"]["feels_like"]
cur_pressure = data["main"]["pressure"]
cur_humidity = data["main"]["humidity"]
cur_visibility = data["visibility"]

print(f"The current weather for {data['name']}:\n"
      f"{weather_img} - {cur_weather}\n"
      f"Temperature: {round(cur_temp,1)}ºC\n"
      f"Feels Like: {round(cur_feels_like,1)}ºC\n"
      f"Pressure: {cur_pressure} hPa\n"
      f"Humidity: {cur_humidity}%\n"
      f"Visibility: {round(cur_visibility/1000)} Km\n")

