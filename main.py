from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# drink = MenuItem()
# drink.name

# 일단.. 어떻게 attributes, methods를 실제로 활용해야 하는지 잘 모르겠다. (강의 듣기)


# CoffeeMaker.report()  >> Class 뒤에 점 표기법을 하면 안된다. (완전 엉터리로 함): 점 표기법은 object 뒤에 사용!!

# coffee_maker = CoffeeMaker()
# menu = Menu()
# menu_item = MenuItem()
# def coffee_machine():
#     order = input(f"What would you like to order? ({menu.get_items()}): ")
#     menu.find_drink(order)
#     # if order == "off":
#     #     return    >>> (프로그램 종료를 해야할 떄) 꼭 return을 사용하지 않아도 while문에서 boolean flag를 이용해도 된다.
#     # elif order == "report":
#     #     coffee_maker.report()
#     # else:
#     #     order = menu_item.name
#     #     if coffee_maker.is_resource_sufficient(menu_item.name):
#     #         print("make coffee")
#     #     else:
#     #         print("Sorry, there is not enough ingredients.")    #>> 어떤 재료가 부족한지 안내하기 >> 이런 것은 클래스 안의 메소드에 이미 포함됨.
#     #         return

is_on = True

menu = Menu()
options = menu.get_items()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while is_on:
    order = input(f"What would you like to order? {options}: ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)    #drink: objeck of MenuItem
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        else:
            is_on = False

