import random as rn
from art import logo
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
correct_guess = rn.choice(list_num)
# print(correct_guess)
print(logo)
print("Computer is thinking a number between 1 and 100. ")
mode_select = input("Select a mode to play. 'Easy' or 'Hard' : ")

game_over = False
Easy_level = 10
Hard_level = 5
while not game_over:
    if Easy_level == 0 or Hard_level == 0:
        game_over = True
        print("You have run out of guess. You lose.")

    else:
        user_guess = int(input("Guess a number between 1 and 100. "))

        def easy():
            global Easy_level
            Easy_level -= 1
            print(f"You have {Easy_level} guesses left. ")

            if correct_guess > user_guess:
                return "Too low."
            elif correct_guess < user_guess:
                return "Too high."

            # for i in range(counter_num):
            #     counter_num -= 1

            # else:
            #     print(f"Your guess is {user_guess} which is {correct_guess} ")

        def hard():
            # counter_num = 4
            # print(f"You have {counter_num} choices. ")
            # for i in range(counter_num):
            global Hard_level
            Hard_level -= 1
            print(f"You have {Hard_level} guesses left. ")

            if correct_guess > user_guess:
                return "Too low."
            elif correct_guess < user_guess:
                return "Too high."

            # counter_num -= 1

            # else:
            #     print(f"Your guess is {user_guess} which is {correct_guess} ")
            return Hard_level - 1

        if mode_select == "Easy":
            print(easy())
        else:
            print(hard())

        if user_guess == correct_guess:

            print(
                f"Your guess is {user_guess} which is {correct_guess}. You Win.  ")
            game_over = True
