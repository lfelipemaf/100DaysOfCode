import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(word_list)
hint = len(word)*"-"
word_guess = []
print(hint)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
letter = input("Guess a word: ")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for l in word:
    if letter.lower() == l:
        word_guess.append(l)
    else:
        word_guess.append("_")
word_guess = ''.join(word_guess)
print(word_guess)