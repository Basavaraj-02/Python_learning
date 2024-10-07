# from turtle import Turtle,Screen
# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("pokemon Name",["pikachu","squirtle","charmander"])
# table.add_column("Type",["Electric","Water","Fire"])

# table.align="c"
# print(table)
# from make import Make,MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
# Coffee_maker = CoffeeMaker()
# money_maker= MoneyMachine()
# menu = Menu()
# is_on = True
# while is_on():
class user:

    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.follwer=0

user_1=user("001","basava")
user_2=user("002","raj")
print(user_1.username)

