#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

import art
import random
import os


def deal_card():
   """Returns a random card from the deck."""
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   card = random.choice(cards)
   return card

def calculate_socre(cards):
     """Calculete the score of the cards"""
     if sum(cards) == 21 and len(cards) == 2:
          return 21
     if 11 in cards and sum(cards) > 21:
          cards.remove(11)
          cards.append(1)
     return sum(cards)

user_cards = []
computer_cards = []

os.system("cls || clear")

start_game = input("Do you wnat to play Blackjack? 'y' or 'n': ").lower()
if start_game == 'y':
    print(art.logo)
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        user_score = calculate_socre(user_cards)
        cpu_score = calculate_socre(computer_cards)

    print(f"\nYour cards: {user_cards}, current score: {user_score}")
    print(f"Computer`s first card: {computer_cards[0]}")
    buy = input("\nType 'y' to get another car, type 'n'to pass: ")
    if buy == 'y':
        user_cards.append(deal_card())
        user_score = calculate_socre(user_cards)
        if cpu_score < 17:
             computer_cards.append(deal_card())
             cpu_score = calculate_socre(computer_cards)

    
    print(f"\nYour cards: {user_cards}, current score: {user_score}")
    print(f"Your cards: {computer_cards}, current score: {cpu_score}")

    if user_score == 21:
         print(f"\nYou have won the game.\n")
    elif user_score > 21:
         print(f"\nYou got busted.\n")
    elif user_score > cpu_score:
         print(f"\nYou have won the game.\n")
    elif user_score == cpu_score:
         print(f"\nIt's a draw.")
    else:
          print(f"\nYou have lost the game.\n")