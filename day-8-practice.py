# def great():
#     print("Practice")
#     print("Something")
#     print("daily")


# great()

# def greet_name(name):
#     print(f"Hello {name}")
#     print(f"How you doin? {name}")


# greet_name("Alu")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")


# greet_with(name="Halum", location="Shundarban")

# import math


# def paint_calc(height, width, cover):
#     num_can = math.ceil((height*width)/cover)
#     print(f"You'll need {num_can} cans of paint.")


# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

def prime_checker(number):
    is_prime = True
    for i in range(2, number):

        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
