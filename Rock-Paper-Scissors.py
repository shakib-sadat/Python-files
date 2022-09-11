import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose_num = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
choose = int(choose_num)


if choose > 2 or choose < 0:
    print("Inavalid Number.")
else:

    if choose == 0:
        print(rock)
    if choose == 1:
        print(paper)
    if choose == 2:
        print(scissors)

    print("Computer chose:")
    com = [rock, paper, scissors]
    com_choose = random.choice(com)
    print(com_choose)
    if com_choose == com[0] and choose == 1:
        print("You win")
    if com_choose == com[0] and choose == 0:
        print("Draw")
    if com_choose == com[0] and choose == 2:
        print("You lose")
    if com_choose == com[1] and choose == 1:
        print("Draw")
    if com_choose == com[1] and choose == 0:
        print("You lose")
    if com_choose == com[1] and choose == 2:
        print("You win")
    if com_choose == com[2] and choose == 1:
        print("You lose")
    if com_choose == com[2] and choose == 0:
        print("You win")
    if com_choose == com[2] and choose == 2:
        print("Draw")
