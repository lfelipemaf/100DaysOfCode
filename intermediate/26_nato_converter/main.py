import pandas
import pandas as pd

nato = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}


name = input("Tell me your name?:  ").upper()

letters =[word for word in name]
nato_name = [nato_dict[letter] for letter in name]
print(nato_name)