alphabet = list("abcdefghijklmnopqrstuvwxyz")

direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
text = input("Enter your message: ").lower()
shift = int(input("Enter shift number: "))

shift = shift % 26

result = ""

if direction == "decode":
    shift = -shift

for letter in text:
    if letter in alphabet:
        position = alphabet.index(letter)
        new_position = (position + shift) % 26
        result += alphabet[new_position]
    else:
        result += letter

print("Result:", result)