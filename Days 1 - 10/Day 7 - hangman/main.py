import words

chosen_word = words.chosen_word
word_length = len(chosen_word)

print(f'\nThe word is: {chosen_word}\n')
print(word_length* "-")
print("\n")
word_guess = []
for _ in range(word_length):
    word_guess += "_"

guess = str(input("Guess a word: ")).lower()
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        word_guess[position]= letter

print(word_guess)