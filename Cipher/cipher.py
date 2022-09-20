from turtle import position
from collections import deque
import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


def caesar(start_text, num_shift, cipher_direction):
    final_text = ""
    # if cipher_direction != "encode" or "decode":
    #     print("Invalid Input")
    # else:
    if cipher_direction == "decode":
        num_shift *= -1
    for char in start_text:
        if char in alphabet:

            x = alphabet.index(char)

            position = x+num_shift
            new_letter = alphabet[position]
            final_text += new_letter
        else:
            final_text += char
    # print(f"The {cipher_direction}d text is "+''.join(final_text))
    print(f"Here's the {cipher_direction}d result: {final_text}")


# def encrypt(plain_text, num_shift):

#     chipher_text = []
#     for letter in plain_text:
#         x = alphabet.index(letter)
#         position = x+num_shift
#         new_letter = alphabet[position]
#         # chipher_text += new_letter
#         chipher_text.append(new_letter)
#     print(f"The encoded text is "+''.join(chipher_text))

#     # items = deque(x)
#     # items.rotate(num_shift)


# def decrypt(chipher_text, num_shift):
#     # plain_text = ""
#     plain_text = []
#     for letter in chipher_text:
#         x = alphabet.index(letter)
#         position = x-num_shift
#         new_letter = alphabet[position]
#         # plain_text += new_letter
#         plain_text.append(new_letter)
#     print(f"The encoded text is "+''.join(plain_text))


# if direction == "encode":
#     encrypt(plain_text=text, num_shift=shift)
# if direction == "decode":
#     decrypt(chipher_text=text, num_shift=shift)
# else:
#     print("Invalid Input.")
continue_dec = True
while continue_dec:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text=text, num_shift=shift, cipher_direction=direction)
    decision = input("Type 'yes' to go again or 'no' to stop.\n")
    if decision == "no":
        continue_dec = False
        print("Goodbye.")
