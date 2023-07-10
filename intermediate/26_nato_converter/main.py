import pandas as pd

nato = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

def generate_phonetic():
    name = input("Tell me your name?:  ").upper()
    try:
        nato_name = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_name)

generate_phonetic()
