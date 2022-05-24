alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(direction, text, shift):

    if direction == "-":
        shift *= -1

    result = ""

    for letter in text:
        if letter not in alphabet:
            result += letter
        else:
            new_index = (alphabet.index(letter)) + shift
            if new_index > 25:
                new_index -= 26
            result += alphabet[new_index]
    print(result)

go_on = True

while go_on:
    choice = input("run cipher program? Y or N?").lower()
    if choice == "y":
        direction = input("encode (+) or decode(-)? ")
        text = input("Your text ").lower()
        shift = int(input("Shift: "))

        cipher(direction, text, shift)
    else:
        go_on = False





