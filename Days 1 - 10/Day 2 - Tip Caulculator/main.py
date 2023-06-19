
bill = input("How much was the bill: ")
people = input("How many people do you want to split the bill: ")
tip_percentage = input("What tip percentage dou you want to pay: ")

tip = float(bill) * (float(tip_percentage)/100)

total = (float(bill) + tip)/ float(people)

print(round(total,2))