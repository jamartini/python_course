# This is a coffee machine simulator. Firstly, it should "check" for the available resources, just like when you turn
# the machine on. Then it asks what you'd like to drink, you enter your coins, and it continues on until you type "off".

# Isto é um simulador de máquina de café. Primeiramente ela "checa" os recursos disponíveis, como quando você liga a
# máquina. Então ela pede o que você vai querer beber, você insere as moedas, e ela continua até que você digite "off".

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0,
}


def calc_amount():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    quarters_total = quarters * 0.25
    dimes = int(input("How many dimes? "))
    dimes_total = dimes * 0.1
    nickels = int(input("How many nickels? "))
    nickels_total = nickels * 0.05
    pennies = int(input("How many pennies? "))
    pennies_total = pennies * 0.01
    total_amount = quarters_total + dimes_total + nickels_total + pennies_total
    return total_amount


def coffee_machine(request):
    if request == 'espresso':
        amount = calc_amount()
        while amount < 1.5:
            print("Sorry, not enough money.")
            amount = calc_amount()
        if ((resources['water'] - 50) >= 0) and ((resources['coffee'] - 18) >= 0):
            resources['water'] -= 50
            resources['coffee'] -= 18
            resources['money'] += 1.5
            print("Here is your espresso!")
            print(f"Here is your ${round(amount - 1.5, 2)} change.")
        elif (resources['water'] - 50) < 0:
            print("Sorry, not enough water.")
        elif (resources['coffee'] - 18) < 0:
            print("Sorry, not enough coffee.")

    if request == 'latte':
        amount = calc_amount()
        while amount < 2.5:
            print("Sorry, not enough money.")
            amount = calc_amount()
        if ((resources['water'] - 200) >= 0) and ((resources['milk'] - 150) >= 0) and ((resources['coffee'] - 24) >= 0):
            resources['water'] -= 200
            resources['milk'] -= 150
            resources['coffee'] -= 24
            resources['money'] += 2.5
            print("Here is your latte!")
            print(f"Here is your ${round(amount - 2.5, 2)} change.")
        elif (resources['water'] - 200) < 0:
            print("Sorry, not enough water.")
        elif (resources['milk'] - 150) < 0:
            print("Sorry, not enough milk.")
        elif (resources['coffee'] - 24) < 0:
            print("Sorry, not enough coffee.")

    if request == 'cappuccino':
        amount = calc_amount()
        while amount < 3:
            print("Sorry, not enough money.")
            amount = calc_amount()
        if ((resources['water'] - 250) >= 0) and ((resources['milk'] - 100) >= 0) and ((resources['coffee'] - 24) >= 0):
            resources['water'] -= 250
            resources['milk'] -= 100
            resources['coffee'] -= 24
            resources['money'] += 3
            print("Here is your cappuccino!")
            print(f"Here is your ${round(amount - 3, 2)} change.")
        elif (resources['water'] - 250) < 0:
            print("Sorry, not enough water.")
        elif (resources['milk'] - 100) < 0:
            print("Sorry, not enough milk.")
        elif (resources['coffee'] - 24) < 0:
            print("Sorry, not enough coffee.")

    if request == 'report':
        print(f"Water: {resources['water']}mL")
        print(f"Milk: {resources['milk']}mL")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money : ${resources['money']}")


def to_continue():
    should_continue = input("What would you like? (espresso/latte/cappuccino): ")
    return should_continue


machine_on = True

while machine_on:
    next_requirement = to_continue()
    if next_requirement == 'off':
        machine_on = False
    else:
        coffee_machine(next_requirement)
