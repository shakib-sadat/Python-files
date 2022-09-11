from itertools import count


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combine_count = (name1+name2)
lower_count = combine_count.lower()

t = lower_count.count('t')
r = lower_count.count('r')
u = lower_count.count('u')
e = lower_count.count('e')

l = lower_count.count('l')
o = lower_count.count('o')
v = lower_count.count('v')
e = lower_count.count('e')

t_count_ = t+r+u+e
l_count_ = l+o+v+e


score = int(str(t_count_)+str(l_count_))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score},you are alright together.")
else:
    print(f"Your score is {score}")
