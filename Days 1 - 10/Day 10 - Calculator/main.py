import art
import os

def add(f_num,s_num):
    return f_num + s_num

def sub(f_num,s_num):
    return f_num - s_num

def multy(f_num,s_num):
    return f_num * s_num

def divide(f_num,s_num):
    return f_num / s_num

ops ={
    "+": add,
    "-": sub,
    "*": multy,
    "/": divide,
}

os.system('cls || clear')
print(art.logo)
end_calc = False

first_num = int(input("What's the first number: "))
while end_calc is not True:
    for symbol in ops:
        print(symbol)
    operation = input("\nPick an operation: ")
    second_num = int(input("What's the next number: "))
    calculation = ops[operation]
    result_calc = calculation(first_num,second_num)
    print(f"{first_num} {operation} {second_num} = {result_calc}")
    run = input(f"Type 'y' to continue calculating with {result_calc}, or 'n' to start a new calculation: ")
    if run == 'y':
        first_num = result_calc
    else:
        end_calc = True
