from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu= Menu()

is_on = True

while is_on :
    options = input(menu.get_items())
    drink = menu.find_drink(options)
    if options == "off" :
        is_on = False
    elif options == "report" :
        coffee_maker.report()
        money_machine.report()
    else :
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        else:
            print('Sorry we are not able to process your drink right now')