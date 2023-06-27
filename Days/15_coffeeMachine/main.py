import controller

operation = False
while not operation:
    action = input("\nHello, what would you like? (Espresso, Latte, Cappuccino): ").lower()

    if action == 'report':
        controller.report()
    elif action == 'exit':
        operation = True
    else:
        controller.make_coffee(action)
