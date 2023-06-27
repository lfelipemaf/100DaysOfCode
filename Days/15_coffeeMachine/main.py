import controller

operation = False
while not operation:
    action = input("Hello, what would you like?\nEspresso\nLatte\nCappuccino\n").lower()

    if action == 'report':
        controller.report()
    elif action == 'exit':
        operation = True
    else:
        controller.make_coffee(action)
