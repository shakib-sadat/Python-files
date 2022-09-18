import random
from turtle import position
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
game_end = False


print(f'Pssst, the solution is {chosen_word}.')

lives = 6

display = []
word_length = len(chosen_word)
for letter in chosen_word:
    display.append("_")


while not game_end:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        game_end = True
        print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_end = True
        print("You win.")

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
