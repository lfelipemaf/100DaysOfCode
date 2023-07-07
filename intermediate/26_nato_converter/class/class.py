# list comprehension
# new_list = [new_item for item in list if test]
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# with open("file1.txt") as file1:
#     file1_list = [int(n) for n in file1]
# with open("file2.txt") as file2:
#     file2_list = [int(n) for n in file2]
# result = [num for num in file1_list if num in file2_list]

# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# word_list = sentence.split()
# result = {word: len(word) for word in word_list}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {weekday: (int(temp_c) * 9/5) + 32 for (weekday, temp_c) in weather_c.items()}
#
# print(weather_f)


# Interate over Pandas DataFrame

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}


# # Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

import pandas as pd

student_df = pd.DataFrame(student_dict)
# # print(student_df)
# for (key, value) in student_df.items():
#     print(key)

for (index, row) in student_df.iterrows():
    if row.student == 'Angela':
        print(row.score)
