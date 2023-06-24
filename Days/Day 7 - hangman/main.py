import words
import images

end_of_game = False
chosen_word = words.chosen_word
print(f"\n{images.logo}\n The word to guess is:\n\n  {len(chosen_word) * '-'}")
word_length = len(chosen_word)
lives = 6
display = []

for _ in range(word_length):
    display += "_"
print(images.stages[lives])
guesses = []
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    if chosen_word.count(guess) == 0:
        lives -= 1
    if guess in guesses:
        print(f"\nAttention! you already guessed the letter {guess}")
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    guesses.append(guess)
    print(images.stages[lives])
    print(f"{' '.join(display)}")
    if "_" not in display and lives > 0:
        end_of_game = True
        print(f"\n{images.win}")
    elif "_" in display and lives == 0:
        end_of_game = True
        print(f"\n{images.lose} \nThe word was {chosen_word}")