import words
def ask():
    letter = str(input("Guess a word: ")).lower()
    return letter
def complete_word(letter_chosen,word_guess):
    letter = letter_chosen
    for l in chosen_word:
        if letter == l:
            word_guess.append(l)
        else:
            word_guess.append("_")
    word_guessed = ''.join(word_guess)
    return word_guessed


chosen_word = words.chosen_word
print(len(chosen_word) * "-")
word_guess = []
letter = ask()

guessed = complete_word(letter, word_guess)
print(guessed)
count = 0
for i in guessed:
    if i == '_':
        count = count + 1
word_guess = guessed


