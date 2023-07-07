import art
import random
import os

def deal_card():
   """Returns a random card from the deck."""
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   card = random.choice(cards)
   return card

def calculate_score(cards):
     """Take the list of cards and return the calculated the score of the cards"""
     if sum(cards) == 21 and len(cards) == 2:
          return 0
     if 11 in cards and sum(cards) > 21:
          cards.remove(11)
          cards.append(1)
     return sum(cards)

def compare(user,cpu):
     """Compare the score between players and return the winner."""
     if user == cpu:
         return "Draw"
     elif cpu == 0:
         return "Lose, dealer has Blackjack"
     elif user == 0:
         return "Win with a Blackjack"
     elif user > 21:
         return "You got busted."
     elif cpu > 21:
         return "Dealer got busted"
     elif user > cpu:
         return "You won"
     else:
         return "You lose"

game =  False
os.system("cls || clear")
start_game = input("Do you wnat to play Blackjack? 'y' or 'n': ").lower()
while not game:
    os.system("cls || clear")
    user_cards = []
    computer_cards = []

    
    if start_game == 'y':
        is_game_over = False
        print(art.logo)
        for i in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(computer_cards)
        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer`s first card: {computer_cards[0]}")

        if user_score == 0 or cpu_score == 0 or user_score >21:
            is_game_over = True
        else:
            buy = input("\nType 'y' to get another car, type 'n'to pass: ")
            if buy == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True

    while cpu_score != 0 and cpu_score <17:
        computer_cards.append(deal_card())
        cpu_score = calculate_score(computer_cards)
            

    print(f"Your cards: {user_cards}. Final score: {user_score}")
    print(f"Dealer cards: {computer_cards}. Final score: {cpu_score}")
    print(compare(user_score,cpu_score))

    restart =  input("Do you wnat to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if restart == 'n':
     game = True   
