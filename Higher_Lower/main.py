import art
from data import data
import random as rn
import os

print(art.logo)

count_score = 0

random_b = rn.choice(data)
# random_a = random_b
game_over = False
while not game_over:

    def compare(rand):
        rand_name = rand["name"]
        rand_description = rand["description"]
        rand_country = rand['country']
        return f"{rand_name}, a {rand_description}, from {rand_country}"

    # def compare():
    #     # rand_key = rn.choice(key)
    #     for key in data:
    #         rand_name = rn.choice((key['name']))
    #         rand_description = rn.choice((key['description']))
    #         rand_country = rn.choice((key['country']))
    #         print((key['name']), (key['description']))

    def guess_ans(guess, a_follower_count, b_follower_count):

        if a_follower_count > b_follower_count:
            return guess == "a"
        else:
            return guess == "b"

    # compare()
    random_a = random_b
    random_b = rn.choice(data)
    while random_a == random_b:
        random_b = rn.choice(data)

    print(f"Compare A : {compare(random_a)}")
    print(art.vs)
    print(f"Compare B : {compare(random_b)}")

    guess = input("Who has more Instagram followers? 'A' or 'B'.").lower()
    a_follower_count = random_a['follower_count']
    b_follower_count = random_b['follower_count']
    is_correct = guess_ans(guess, a_follower_count, b_follower_count)

    os.system('cls')
    print(art.logo)

    if is_correct:
        count_score += 1
        # random_b = rn.choice(data)
        # random_a = random_b
        print(f"You're right!! Current score : {count_score}")

    else:
        game_over = True
        print(f"Sorry, you're wrong. Final score is {count_score}")
