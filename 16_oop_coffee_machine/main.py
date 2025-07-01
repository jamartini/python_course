# This is an OOP version of the project number 15, the coffee machine simulator.

# Esta é uma versão em POO do projeto número 15, o simulador de máquina de café.

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
coffee = Menu()
machine = CoffeeMaker()
payment = MoneyMachine()

while machine_on:
    order = input(f"What would you like? ({coffee.get_items()}): ")
    if coffee.find_drink(order) is None:
        if order == 'report':
            machine.report()
            payment.report()
        elif order == 'off':
            machine_on = False
    else:
        coffee = coffee.find_drink(order)
        if machine.is_resource_sufficient(coffee):
            if payment.make_payment(coffee.cost):
                machine.make_coffee(coffee)
                coffee = Menu()
            else:
                coffee = Menu()
        else:
            coffee = Menu()
