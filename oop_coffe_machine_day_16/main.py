from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_run = True

menu_operations = Menu()
money_operations = MoneyMachine()
coffee_operations = CoffeeMaker()

while is_run:
  user_input = input("What would you like? (espresso/latte/cappuccino): ")
  if user_input == "report":
    print(coffee_operations.report())
    print(money_operations.report())
  else:
    drink = menu_operations.find_drink(user_input)
    if drink:
      cost = drink.cost
      is_payable = money_operations.make_payment(cost)
      if is_payable:
        is_sufficient = coffee_operations.is_resource_sufficient(drink)
        if is_sufficient:
          coffee_operations.make_coffee(drink)
        else:
          is_run = is_sufficient