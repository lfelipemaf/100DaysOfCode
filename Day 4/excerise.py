# Randomisation
import random
import my_module
# c = random.randint(1,10)
# print(c)
# print(my_module.pi)
#
# d = random.random()
#
# print(d)
#
# a = round(d * c,2)
# print(a)
#
# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}")

# head_or_tails = random.randint(0,1)
# if head_or_tails == 1:
#     print("Heads")
# else:
#     print("Tails")


# exercise 2

# # Import the random module here
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# n = random.randint(0, len(names) - 1)
# print(f"{names[n]} is going to buy the meal today!")
#
#
# fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
# vegetables = ["Spinach","Kale","Tomatoes","Potatoes","Celery"]
#
# print(type(fruits))
#
# dirty_dozen = [fruits,vegetables]
#
# print(dirty_dozen)
#
# print(dirty_dozen[0][3])
#
# print(dirty_dozen[1][4])
#
# print(len(dirty_dozen)

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
c = position[0]
r = position[1]

map[int(r)-1][int(c)-1] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")





