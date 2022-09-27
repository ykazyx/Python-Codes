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

money = 0
# for keys in MENU:
#     for key in MENU[keys]["ingredients"]:
#         print(key)

choice = "on"
while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        for keys in resources:
            print(f"{keys[0].upper()+keys[1:]}: {resources[keys]}")
        print(f"Money: ${money}")
    elif choice == "off":
        break
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        excess = 0
        for key in MENU[choice]["ingredients"]:
            if MENU[choice]["ingredients"][key] > resources[key]:
                excess = 1
                break
        if excess == 0:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            cm = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            if cm >= MENU[choice]["cost"]:
                for key in MENU[choice]["ingredients"]:
                    resources[key] -= MENU[choice]["ingredients"][key]
                money += MENU[choice]["cost"]
                cm -= MENU[choice]["cost"]
                print(f"Here is ${round(cm,2)} in change.")
                print(f"Here is your {choice} ☕. Enjoy!")
            else :
                print("Sorry that's not enough money.")
        else:
            print("Sorry there is not enough water.")
    else:
        print("Wrong Choice. Try Again")