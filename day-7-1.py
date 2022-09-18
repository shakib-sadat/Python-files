# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess = ").lower()

for letter in chosen_word:
    if letter == guess:
        print("True")
    else:
        print("False")
