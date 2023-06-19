import words

chosen_word = words.chosen_word
word_length = len(chosen_word)

end_of_game = False

print(f'\nThe word is: {chosen_word}\n')
print(word_length* "-")
print("\n")
word_guess = []
for _ in range(word_length):
    word_guess += "_"
live = 6
print(words.stages[live])
while not end_of_game:
    guess = str(input("Guess a word: ")).lower()

    if chosen_word.count(guess) == 0:
        live -= 1
    print(words.stages[live])
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            word_guess[position]= letter
    display = ''.join(word_guess)
    print(display)

    if "_" not in display and live > 0:
        end_of_game = True
        print("You win.")
    elif "_"  in display and live == 0:
        end_of_game = True
        print("You lose.")