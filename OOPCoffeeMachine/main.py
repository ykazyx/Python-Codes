from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

test = Menu()
testreport = CoffeeMaker()
money = MoneyMachine()
choice = 'on'

while choice != 'off':
    choice = input(f"What would you like? {test.get_items()}: ")
    if choice == "report":
        testreport.report()
        money.report()
    elif choice == "off":
        break
    else:
        drink = test.find_drink(choice)
        if testreport.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                testreport.make_coffee(drink)
