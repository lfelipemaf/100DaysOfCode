import os

os.system('cls || clear')

################### Scope ####################

# #local

# def drink_posion():
#   potion_strength = 2 -- local variable
#   print(potion_strength)

# drink_posion()


#global

# player_health = 10 -- global variable

# def game():
#     def drink_posion():
#     potion_strength = 2
#     print(player_health)

# drink_posion()

# #There is no Block Scope
# game_level = 3
# enemies = ['Skeletons','Zombie','Alien']

# if game_level < 5:
#     new_enemy = enemies[0]

# Modifying Global Scope

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global Constants
#Just type as upper case

PI = 3.1415
URL = "www.globo.com"



