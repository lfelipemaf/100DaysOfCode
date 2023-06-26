"""
### PROGRAM REQUIREMENTS ###
1. print report
2. check resources are sufficient?
3. process coins
4. check transaction successful?
5.Make coffee
"""
import controller



def make_coffee(command):
    """Simply make the coffee"""
    response = controller.check_resources(water=controller.MENU[command]['ingredients']['water'], milk=controller.MENU[command]['ingredients']['milk'],coffee=controller.MENU[command]['ingredients']['coffee'])
    if response:
        controller.resources['water'] = controller.resources['water'] - controller.MENU[command]['ingredients']['water']
        controller.resources['milk'] = controller.resources['milk'] - controller.MENU[command]['ingredients']['milk']
        controller.resources['coffee'] = controller.resources['coffee'] - controller.MENU[command]['ingredients']['coffee']

    print(controller.resources)




def process_coins():
    return



action = input("Hello, what would you like?\nEspresso\nLatte\nCappuccino\n").lower()

if action == 'report':
    controller.report()
else:
    make_coffee(action)