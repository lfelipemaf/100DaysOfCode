import art
import random
import os

os.system('cls || clear')

def compare(guess, answer):
    if guess == answer:
        return print(f"\nCongratulation! You gussed the right number: {answer}\n")
    elif guess > answer and guess-answer > 5:
        return print(f"Too high")
    elif guess > answer and guess-answer <= 5:
        return print(f"You are just a little bit high, but really close")
    elif guess < answer and answer-guess <= 5:
        return print(f"You are just a little bit low, but really close")
    else:
        return print(f"Too low")


print(art.logo)
print("Welcome to the Number Gussing Game")
level = input("What lave do you want to play: 'easy' or 'hard': ").lower()

if level == 'easy':
    life = 10
else:
    life = 5

number = random.randint(1,100)
print(f"Testing the code {number}")

for i in range(life):
    print(f"\n{art.heart*life}")
    ask = int(input(f"\nTell me a number between 1 to 100:"))
    compare(guess=ask,answer=number)
    if ask == number:
        break
    life -= 1
    if life == 0 and ask != number:
        print(f"\nGame over\nThe awnser was: {number}\n")