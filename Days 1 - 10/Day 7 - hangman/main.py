import words

end_of_game = False
chosen_word = words.chosen_word
print("\n")
print("""#     #    #    #     #  #####  #     #    #    #     # 
#     #   # #   ##    # #     # ##   ##   # #   ##    # 
#     #  #   #  # #   # #       # # # #  #   #  # #   # 
####### #     # #  #  # #  #### #  #  # #     # #  #  # 
#     # ####### #   # # #     # #     # ####### #   # # 
#     # #     # #    ## #     # #     # #     # #    ## 
#     # #     # #     #  #####  #     # #     # #     #""")
print(f"\n The word to guess is:\n\n  {len(chosen_word) * '-'}")
word_length = len(chosen_word)
lives = 6
display = []
for _ in range(word_length):
    display += "_"
print(words.stages[lives])
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    if chosen_word.count(guess) == 0:
        lives -= 1
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(words.stages[lives])
    print(f"{' '.join(display)}")
    if "_" not in display and lives > 0:
        end_of_game = True
        print("You win.")
    elif "_" in display and lives == 0:
        end_of_game = True
        print("You lose.")