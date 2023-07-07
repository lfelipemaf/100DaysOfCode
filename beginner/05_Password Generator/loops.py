# # fruits = ["apple","banana","peach","pear"]
# # for fruit in fruits:
# #     print(fruit)
#
# # Exercise 1
#
# student_heights = entry("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# a = 0
# for l in student_heights:
#   a += l
# print(round(a/len(student_heights)))
#
# # Exercise 2
#
# # 🚨 Don't change the code below 👇
# student_scores = entry("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
# max = 0
# for m in student_scores:
#   if m >= max:
#     max = m
#   else:
#     max
#

# print(f"The highest score in the class is: {max}")

# # Exercise 3
# total = 0
# for number in range(2,101,2):
#   total += number
# print(total)

# exercise 4
# Your program should print each number from 1 to 100 in turn.
#
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#
#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

number = 0
for n in range(1,101):
  if n % 3 == 0 and n % 5 != 0:
    print("Fizz")
  elif n % 3 != 0 and n % 5 == 0:
   print("Buzz")
  elif n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
  else:
    print(n)