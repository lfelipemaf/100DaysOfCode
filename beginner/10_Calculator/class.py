
def format_name(first_name,last_name):
    """Return the full name in title case."""
    if first_name == '' or last_name == '':
        return "You did not provide valid inputs:"
    f_name = first_name.title()
    l_name = last_name.title()
    return f"{f_name} {l_name}"


print(format_name(input("What is your first name?\n"),input("What is your last name?\n")))

# Exercise 1 - Days in Month 
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year,month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(year) == True:
#     if month == 2:
#         return month_days[month-1] + 1
#     else:
#       return month_days[month-1]
#   else:
#      return month_days[month-1]

  
# #🚨 Do NOT change any of the code below 
# year = int(entry("Enter a year: "))
# month = int(entry("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
