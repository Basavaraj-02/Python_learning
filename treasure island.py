print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print('welcome to treasure island.')
print("your mission is to find the treasure.")
choice1=input('you\'re at a crossroad,where do you want to go? type "left" or "roght".')
if choice1 =="left":
    choice2=input('you\'ve come to a lake.there is an the middle of teh lake. Type"wait" to wait for a boat.'
           'Type "swim" to swim across.').lower()
    if choice2 =="wait":
        choice3=input("you arrive at the island unharmed.there id houde with 3 doors.one red,one yellow and one blue.which color do you choose?").lower()
        if choice3 =="red":
            print("it's a room full of fire.game over")
        elif choice3 =="yellow":
            print("you found the treasure.you win!")
        elif choice3 =="blue":
            print("you enter a room of beasts.game over.")
        else:
            print("you choose a door doesn't exist.game over.")
        #game will continue
    else:
        print("you got attacked by an angry trout.game over")
else:
    print("you fell in to a hole.game over.")


