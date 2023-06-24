import misc

print(misc.logo)
end = False



def ceaser(plain_text, shift_amount, direction):
    text = ""
    if direction == 'decode':
        shift_amount *= -1
    for letter in plain_text:
        position = misc.alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = misc.alphabet[new_position]
        text += new_letter
    print(f"Your {direction}d message:\n{text}.")


while not end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    misc.alphabet += misc.alphabet * shift

    ceaser(plain_text=text, shift_amount=shift, direction=direction)

    continue_run = input("Do you want to continue: 'y' for  Yes or 'n' for No:\n")

    if continue_run == 'n':
        end = True
