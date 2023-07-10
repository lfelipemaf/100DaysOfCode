# Handling with errors

# try:
#     file = open("file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"This {error_message} key does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up")
#
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
# bmi = weight / height ** 2
# print(bmi)
#
# # exercise 1 - IndexError Handling
# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)
# # exercise 2 - KeyError Handling
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes += post['Likes']
#     except KeyError:
#         pass
#
#
# print(total_likes)

# ----------------------------------- JSON ----------------------------------- #
# write -> json.dump()
# read -> json.load()
# update -> json.update()
