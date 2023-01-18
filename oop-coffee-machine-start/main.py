from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem

money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()

    choice = input(f"What do you want? ({options}): ")

    if choice == 'off':
        is_on = False

    elif choice == 'report':
        coffee_machine.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
