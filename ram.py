print("welcome to the tollercoaster!")
height=int(input("what is your height in cm?"))
bill=0
if height >=120:
    print("you can ride the tollercoaster")
    age=int(input("what is your age?"))
    if age >=12:
        bill=5
        print("child tickets are $5")
    elif age >=18:
        bill=7
        print("youth tickets are $7")
    else:
         bill=12
         print("adult tickets are $12")
    wants_photo=input("do you want to have a photo take? type Y for Yes and N for No")
    if wants_photo =="Y":
        bill +=bill
        print(f"your final bill is{bill}")


    print("sorry you have to grow taller before you can ride")
