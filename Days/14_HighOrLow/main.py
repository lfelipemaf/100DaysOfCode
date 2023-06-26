import art
import random
from game_data import data
import os

def choose_data():
    """Return a random option to the game."""
    i = data[random.randint(0, 49)]
    name = i['name']
    description = i['description']
    country = i['country']
    follower_count = int(i['follower_count'])
    return name, description, country,follower_count


a = choose_data()
b = choose_data()

end_game = False
score = 0

while not end_game:
    os.system('cls || clear')
    print(art.logo)
    print(f"A: {a[0]}, {a[1]}, {a[2]}")
    print(art.vs)
    print(f"B: {b[0]}, {b[1]}, {b[2]}")
    print(f"Score: {score}")
    user_input = input("\nWho has more followers on instagram A or B: ").lower()
    if user_input == 'a' and a[3] > b[3]:
        score += 1
        b = choose_data()
    elif user_input == 'b' and a[3] < b[3]:
        score += 1
        a = choose_data()
    else:
        end_game = True
        print(f"\nOh no! That's game over.\nYour final score is {score}\n")

