import random
import os

import hangman_art
import hangman_word
word_list = hangman_word.word_list

stages = hangman_art.stages
# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
game_end = False
lives = 6

print(hangman_art.logo)


display = []
word_length = len(chosen_word)
for letter in chosen_word:
    display.append("_")


while not game_end:
    guess = input("Guess a letter: ").lower()
    os.system('cls')

    if guess in display:
        print(f"You've already guessed {guess}\n")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(guess+" is not in the word. So, you lose a life ;)\n")
        lives -= 1
    if lives == 0:
        game_end = True
        print("You lose!!!!!!\n")
        print(f'The solution is {chosen_word}.')

    print(f"{' '.join(display)}\n")

    if "_" not in display:
        game_end = True
        print("You win.")
    print(f"You have {lives} tries remaining.\n")

    print(stages[lives])

    #fill_display = display.append(letter)
    # if lives == 6:
    #     print(stages[6])
    # if lives == 5:
    #     print(stages[5])
    # if lives == 4:
    #     print(stages[4])
    # if lives == 3:
    #     print(stages[3])
    # if lives == 2:
    #     print(stages[2])
    # if lives == 1:
    #     print(stages[1])
    # if lives == 0:
    #     print(stages[0])
