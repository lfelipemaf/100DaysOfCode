# def greet(name, age, city):
#     print(f"\nHello {name},\nYou are {age} years old and live in {city}.")
#
#
# name = entry("What's your name?\n")
# age = entry("How old are you?\n")
# city = entry("Where do you live?\n")
#
#
# greet(city=city,age=age,name=name)
#
# # Exercise 1 - Paint Area Calculator
# import  math
# def paint_calc(height,width,cover):
#     n_of_cans=((height*width)/cover)
#     print(f"You'll need {int(math.ceil(n_of_cans))} cans of paint.")
#
# test_h = int(entry("Height of wall: "))
# test_w = int(entry("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Exercise 2 - Prime number
# Write your code below this line 👇
# def prime_checker(number):
#     prime = []
#     for n in range(1,number+1):
#         if number % int(n) == 0:
#            prime.append(True)
#         else:
#             prime.append(False)
#     if prime.count(True) == 2:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
#
# # Write your code above this line 👆
#
# # Do NOT change any of the code below👇
# n = int(entry("Check this number: "))
# prime_checker(number=n)

fruits = ['apple', 'banana', 'cherry']
print(fruits)
for i in range(-1,1):
  fruits.pop(i)
  print(fruits)
