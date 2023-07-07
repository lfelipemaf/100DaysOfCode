def report():
    """Returns the report of all the available resources"""
    print(f"\nWater: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}\n")


def check_resources(water, milk, coffee):
    if resources['water'] >= water and resources['milk'] >= milk and resources['coffee'] >= coffee:
        return True
    else:
        return False


def process_coins(drink):
    print(f"\nOk, the {drink.title()} is ${MENU[drink]['cost']}")
    penny = float(input("\nHow Many pennies?")) * 0.01
    nickels = float(input("How Many nickels?")) * 0.05
    dimes = float(input("How Many dimes?")) * 0.10
    quarter = float(input("How Many quarter?")) * 0.25
    amount_inserted = penny + nickels + dimes + quarter
    if amount_inserted >= MENU[drink]['cost']:
        change = amount_inserted - MENU[drink]['cost']
        print(f"Thank you, you have inserted ${round(amount_inserted,2)} and your ${round(change,2)} is now at the "
              f"disposal.")
        return True
    else:
        print(f"Sorry, not enough money. You have inserted ${round(amount_inserted,2)} Pick up your coins at the "
              f"disposal.")
        return False


def make_coffee(command):
    """Simply make the coffee"""
    resources_response = check_resources(water=MENU[command]['ingredients']['water'],
                                         milk=MENU[command]['ingredients']['milk'],
                                         coffee=MENU[command]['ingredients']['coffee'])
    if resources_response:
        coins_response = process_coins(command)
        if coins_response:
                resources['water'] -= MENU[command]['ingredients']['water']
                resources['milk'] -= MENU[command]['ingredients']['milk']
                resources['coffee'] -= MENU[command]['ingredients']['coffee']
                resources['money'] += MENU[command]['cost']
    else:
        print("Sorry, not enough resources")


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}
