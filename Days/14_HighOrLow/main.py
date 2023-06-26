import art
import random
from game_data import data
import os

def choose_data(options):
    """Return a random option to the game."""
    i = random.choice(options)
    d = data[i]
    name = d['name']
    description = d['description']
    country = d['country']
    follower_count = int(d['follower_count'])
    return name, description, country,follower_count,i
def start_game():
    options = []
    for i in range(0, len(data)):
        options.append(i)
    return options


o = start_game()
a = choose_data(o)
o.remove(a[4])
b = choose_data(o)
o.remove(b[4])
end_game = False
score = 0

while not end_game:
    os.system('cls || clear')
    print(art.logo)
    print(f"A: {a[0]} - {a[2]}\n{a[1]}")
    print(art.vs)
    print(f"B: {b[0]} - {b[2]}\n{b[1]}")
    print(f"Score: {score}")
    user_input = input("\nWho has more followers on instagram A or B: ").lower()
    if user_input == 'a' and a[3] > b[3]:
        score += 1
        b = choose_data(o)
        o.remove(b[4])
    elif user_input == 'b' and a[3] < b[3]:
        score += 1
        a = choose_data(o)
        o.remove(a[4])
    else:
        end_game = True
        print(f"\nOh no! That's game over.\nYour final score is {score}\n")