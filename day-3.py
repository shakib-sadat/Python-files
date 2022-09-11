height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("children ticket $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket $7")
    elif age >= 45 & age <= 55:
        print("You do not have to pay")
    else:
        bill = 12
        print("adult ticket $12")

    photo = input("Do you want photo taken? Y or N.")

    if photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry you can not ride ;)")
