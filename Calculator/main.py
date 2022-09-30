from art import logo
# Calculator

# Add


def add(n1, n2):
    return n1+n2

# Sub


def sub(n1, n2):
    return n1 - n2

# Mul


def mul(n1, n2):
    return n1*n2

# div


def div(n1, n2):
    return n1/n2


operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    print(logo)
    num1 = float(input("What is your first number?: "))

    for (key) in operation:
        print(key)

    flag_continue = True

    while flag_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation = operation[operation_symbol]
        ans = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {ans}")

        if input(f"Type 'y' to continue calculating with {ans} or Type 'n' to start a new calculation : ") == "y":
            num1 = ans
        else:
            flag_continue = False
            calculator()


            # print(f"{num1} {operation_symbol} {num2} = {ans}")
calculator()
