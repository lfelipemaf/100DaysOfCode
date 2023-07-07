# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# type(data)
#
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data["temp"].mean())
# print(data["temp"].max())
#
#
# #Get Data in Columns
# print(data["day"])
# print(data.day)


# Get Data in Row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# # print(monday.condition)
#
# temp_celcius = int(monday.temp)
# temp_fahrenheit = ((temp_celcius/5)*9)+32
# print(f"\n{round(temp_celcius,2)}ºC\n{round(temp_fahrenheit,2)}ºF")

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("df.csv")