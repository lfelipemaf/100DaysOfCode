PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        person = name.strip("\n")
        new_letter = letter_contents.replace(PLACEHOLDER, person)
        with open(f"./Output/ReadyToSend/letter_to_{person.replace(' ', '_')}.txt", mode="w") as final:
            final.write(f"{new_letter}")
