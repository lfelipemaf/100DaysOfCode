def report():
    """Returns the report of all the available resources"""
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['water']}\n")

def check_resources(water,milk,coffee):
    if resources['water'] < water or resources['milk'] < milk or resources['coffee'] < coffee:
        return False
    else:
        return True




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

print(MENU["espresso"]['ingredients']['water'])

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}