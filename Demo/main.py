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
    "money": 0.00,
}


def enough_coinage(price, choice):
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickels = input("How many nickels?: ")
    pennies = input("How many pennies?: ")
    total_inserted = .25 * float(quarters) + .10 * float(dimes) + .05 * float(nickels) + .01 * float(pennies)
    # TODO: 6. Check transaction successful?
    if total_inserted < price:
        print('Insufficient funds, money refunded')
    else:
        # TODO: 7. Make Coffee.
        change = total_inserted - price
        print('Here is your ', choice, ' and here is your change ', f'{change:.2f}')
        resources['water'] -= MENU[choice]['ingredients']['water']
        resources['milk'] -= MENU[choice]['ingredients']['milk']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']
        resources['money'] += price

drink_served = False

while not drink_served:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
    coffee_choice = input("What would you like (espresso/latte/cappuccino):")
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if coffee_choice == 'off':
        break
    # TODO: 3. Print report.
    elif coffee_choice == 'report':
        print(resources)
    # TODO: 4. Check resources sufficient?
    else:
        if resources['water'] < MENU[coffee_choice]['ingredients']['water']:
            print('Insufficient water')
        elif resources['milk'] < MENU[coffee_choice]['ingredients']['milk']:
            print('Insufficient milk')
        elif resources['coffee'] < MENU[coffee_choice]['ingredients']['coffee']:
            print('Insufficient coffee')
        else:
            # TODO: 5. Process coins.
            cost = MENU[coffee_choice]['cost']
            print('Please insert: ', cost, 'dollars')
            enough_coinage(cost, coffee_choice)


