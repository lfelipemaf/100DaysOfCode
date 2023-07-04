
with open("./Input/Letters/starting_letter.txt") as letter:
    with open("./Input/Names/invited_names.txt") as names:
            invited = names.readlines()
            text = letter.readlines()
            for name in invited:
                person = name.strip("\n")
                complete_letter = []
                for lines in text:
                    lines.replace("[name]", person)
                    complete_letter.append(lines)
                with open(f"./Output/ReadyToSend/letter_to_{person}.txt", mode="w") as final:
                    final.write(f"{complete_letter}")

