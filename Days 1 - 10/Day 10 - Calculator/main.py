import art
import os

def result(f_num,op,s_num):
    if f_num == '' or op == '' or s_num == '':
        return "You did not privide enought info."
    elif op == '+':
        return float(f_num) + float(s_num)
    elif op == '-':
        return float(f_num) - float(s_num)
    elif op == '*':
        return float(f_num) * float(s_num)
    elif op == '/':
        return float(f_num) / float(s_num)
    else:
        return "Wrong operation sign."
    

os.system('cls || clear')
print(art.logo)
end_calc = False

first_num = input("What's the first number: ")
while end_calc is not True:
    operation = input("\n+\n-\n*\n/\nPick an operation: ")
    second_num = input("What's the next number: ")
    result_calc = result(first_num,operation,second_num)
    print(f"{first_num} {operation} {second_num} = {result_calc}")
    run = input(f"Type 'y' to continue calculating with {result_calc}, or 'n' to start a new calculation: ")
    if run == 'y':
        first_num = result_calc
    else:
        end_calc = True
