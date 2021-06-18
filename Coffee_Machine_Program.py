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
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}


# check if resources are sufficient
def sufficient_resources(menu, drink, resources):
    """This function checks if there are sufficient resources to make the drink and returns True/False"""
    menu['espresso']['ingredients']['milk'] = 0  # because espresso doesn't need any milk
    if resources['Water'] < menu[drink]['ingredients']['water']:
        print("Sorry there isn't enough water to make the drink.")
        return False
    elif resources['Milk'] < menu[drink]['ingredients']['milk']:
        print("Sorry there isn't enough milk to make the drink.")
        return False
    elif resources['Coffee'] < menu[drink]['ingredients']['coffee']:
        print("Sorry there isn't enough coffee to make the drink.")
        return False
    else:
        return True


# process coins
def process_coins():
    """This functions processes the entire amount of money entered by the user and returns the total amount"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickels = int(input("How many nickels?:"))
    pennies = int(input("How many pennies?:"))
    total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total_amount


# check if transaction successful
def check_transaction(menu, drink, resources):
    """This function checks whether the amount user entered is enough for the drink they want and gives change if any"""
    customer_money = process_coins()
    drink_cost = menu[drink]['cost']
    if customer_money < drink_cost:
        print("Sorry that's not enough money.Money refunded")
        return False
    else:
        if customer_money > drink_cost:
            change = round((customer_money - drink_cost), 2)
            print(f"Here is your ${change} in change")
        resources['Money'] += drink_cost
        return True


# make coffee
def make_coffee(drink, resources, menu):
    """This function makes the coffee and deducts the resources used when making the drinks"""
    resources['Water'] -= menu[drink]['ingredients']['water']
    resources['Milk'] -= menu[drink]['ingredients']['milk']
    resources['Coffee'] -= menu[drink]['ingredients']['coffee']
    print(f'Here is your {drink} ☕.Enjoy!')


machine_on = True
# ask user what they want
while machine_on:
    order = input("What would you like?(espresso/latte/cappuccino):")
    drink = 0
    # have option to turn off machine
    if order == "off":
        print("Machine is now under maintenance")
        machine_on = False
        continue
    # print report
    elif order == "report":
        for resource, value in resources.items():
            print(f"{resource} : {value}")
        continue
    elif order == "espresso":
        drink = "espresso"
    elif order == "latte":
        drink = "latte"
    elif order == "cappuccino":
        drink = "cappuccino"
    sufficient_products = sufficient_resources(MENU, drink, resources)
    if sufficient_products:
        if check_transaction(MENU, drink, resources):
            make_coffee(drink, resources, MENU)
        else:
            continue
    else:
        continue
