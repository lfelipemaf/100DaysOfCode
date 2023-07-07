# print("welcome to the roller coaster!")
#
# height = int(entry("What is your height in cm?"))
# age = int(entry("How old are you? "))
# bill = 0
# if height >= 120:
#     print("You can ride the roller coaster!")
#     if age < 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7
#     elif age >= 45 & age <= 55:
#         bill = 0
#     else:
#         bill = 12
#     print("You total bill is $"+ str(bill))
# else:
#     print("Sorry, you can not ride the roller coaster yet!")


#
#
# # Exercise 1 - Odd or Even
#
# # 🚨 Don't change the code below 👇
# number = int(entry("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# if number%2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

#  # Exercise 2 - BMI 2.0
# # 🚨 Don't change the code below 👇
# weight = float(entry("enter your weight in kg: "))
# height = float(entry("enter your height in m: "))
#
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# bmi = round(float(weight)/(float(height) ** 2))
# if bmi <= 18.5:
#     print("Your BMI is "+ str(bmi) +", you are underweight.")
# elif bmi <= 25:
#     print("Your BMI is " + str(bmi) + ", you have a normal weight.")
# elif bmi <= 30:
#     print("Your BMI is " + str(bmi) + ", you are slightly overweight.")
# elif bmi <= 35:
#     print("Your BMI is " + str(bmi) + ", you are obese")
# else:
#     print("Your BMI is " + str(bmi) + ", you are clinically obese.")
#  # exercise 3 - leap year
#
# # 🚨 Don't change the code below 👇
# year = int(entry("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0 | year % 400 != 0:
#         print("Leap year.")
#     else:
#         print("Not leap year.")
# else:
#     print("Not leap year.")
# exercise 4 - Pizza Order Practice
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = entry("What size pizza do you want? S, M, or L ")
# add_pepperoni = entry("Do you want pepperoni? Y or N ")
# extra_cheese = entry("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# if size.upper() == 'S':
#     bill = 15
#     if add_pepperoni.upper() == 'Y':
#         bill = bill + 2
#     else:
#         bill = bill
# elif size.upper() == 'M':
#     bill = 20
#     if add_pepperoni.upper() == 'Y':
#         bill = bill + 3
#     else:
#         bill = bill
# else:
#     bill = 25
#     if add_pepperoni.upper() == 'Y':
#         bill = bill + 3
#     else:
#         bill = bill
# if extra_cheese.upper() == 'Y':
#     bill = bill + 1
# else:
#     bill = bill
# print("Your final bill is: $" + str(bill)+".")

# exercise 5 - Love Calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_names = (name1 + name2).lower()
true_score = 0
love_score = 0
for letter in set("true"):
  true_score += combined_names.count(letter)
for letter in set("love"):
  love_score += combined_names.count(letter)
total_score = int(str(true_score) + str(love_score))
if total_score < 10 or total_score > 90:
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}")

