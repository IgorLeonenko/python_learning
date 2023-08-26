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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def check_resources(choosed_drink):
  values = []
  not_enough_list = []
  for k, v in MENU[choosed_drink]['ingredients'].items():
    if k in resources:
      if resources[k] > v:
        values.append(1)
      else:
        values.append(0)
        not_enough_list.append(k)
  if all(v == 1 for v in values):
    return [True]
  else:
    return [False, not_enough_list]

def check_payment(choosed_drink):
  print('Insert coins:')
  quarters = int(input('quarters: '))
  dimes = int(input('dimes: '))
  nickles = int(input('nickles: '))
  pennies = int(input('pennies: '))
  total_paid = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
  drink_cost = MENU[choosed_drink]['cost']
  if total_paid >= drink_cost:
    resources['water'] -= MENU[choosed_drink]['ingredients']['water']
    if 'milk' in MENU[choosed_drink]['ingredients']:
      resources['milk'] -= MENU[choosed_drink]['ingredients']['milk']
    resources['coffee'] -= MENU[choosed_drink]['ingredients']['water']
    resources['money'] += drink_cost
    if total_paid > drink_cost:
      change_money = total_paid - drink_cost
    else:
      change_money = 0
    return [True, change_money]
  else:
    return False


def coffe_machine_start():
  is_run = True

  while is_run:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input in list(MENU):
      resource_checker = check_resources(user_input)
      if resource_checker[0]:
        payment = check_payment(user_input)
        if payment[0]:
          print(f"Here is your {user_input}. Enjoy!")
          if payment[1] > 0:
            print(f"Here is ${payment[1]} dollars in change.")
        else:
          print("Sorry there is not enough money")
      else:
        print(f"Sorry there is not enough {resource_checker[1]}")
        is_run = False
    elif user_input == "raport":
      for k, v in resources.items():
        print(f"{k}: {v}\n")
    elif user_input == 'off':
      is_run = False

coffe_machine_start()