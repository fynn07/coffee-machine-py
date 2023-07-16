from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_choices = menu.get_items()

progress = True
while progress == True:
  choice = input(f"What would you like? {coffee_choices}? ").lower()
  
  if choice == "report":
    coffee_maker.report()
    money_machine.report()

  else:
    
    if choice == "off":
      print("Thank you for using the Coffee Machine.")
      break
  
    choice = menu.find_drink(choice)
    
    if coffee_maker.is_resource_sufficient(choice) != True:
      print("Resources Insufficient")
    else: 
      n = money_machine.make_payment(choice.cost)
      if n == True:
        coffee_maker.make_coffee(choice)
      