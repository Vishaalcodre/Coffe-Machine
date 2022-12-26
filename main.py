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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def sufficient_resource(drink):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in drink:
        if drink[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction(money, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money >= drink_cost:
        change = round(money-drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee (drink_name, ingredient):
    """Deduct the required ingredients from the resources."""
    for item in ingredient:
        resources[item] -= ingredient[item]

    print(f"Here is your {drink_name} ☕!")


off = False

while not off:
    usr_choice = input("What would you like? (espresso/latte/cappuccino):")

    if usr_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif usr_choice == 'off':
        off = True

    else:
        drink = MENU[usr_choice]
        if sufficient_resource(drink['ingredients']):
            payment = process_coins()
            if transaction(payment, drink['cost']):
                make_coffee(usr_choice, drink['ingredients'])
