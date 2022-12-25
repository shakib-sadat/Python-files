MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

total_money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resource(order_ind):
    """Returns true when order can be made false when there's not enough resources"""
    for item in order_ind:
        if order_ind[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def check_coin():
    """Returns total calculated coins from customers"""
    print("Insert Coins: ")
    total = int(input("how many quaters?: "))*0.25
    total += int(input("how many dimes?: "))*0.1
    total += int(input("how many nickles?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    return total


def is_transaction_succ(money_rec, drink_cost):
    """Return True when payment successful"""
    if money_rec >= drink_cost:
        change = round(money_rec - drink_cost, 2)
        print(f"Here is your ${change}")
        global total_money
        total_money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ind):
    """deduct resources after making coffee"""
    for item in order_ind:
        resources[item] -= order_ind[item]
    print(f"Here is your {drink_name} !! Enjoy !! ")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "latte":
        print(f"{choice} price is $2.5")
    if choice == "espresso":
        print(f"{choice} price is $1.5")
    if choice == "cappuccino":
        print(f"{choice} price is $3.0")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${total_money}")
    else:
        drink = MENU[choice]
        if check_resource(drink["ingredients"]):
            total_money = check_coin()
            if is_transaction_succ(total_money, drink['cost']):
                make_coffe(choice, drink["ingredients"])
