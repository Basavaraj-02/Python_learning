print("welcome to python pizza deliveries!")
size=input("what size pizza do you want? S,M or L:")
pepperoni=input("do you want pepperoni on your pizza? Y or N:")
extra_cheese=input("do you want extra cheese? Y or N: ")
#todo:work out how much they to pay based on their size choice.
bill=0
if size =="S":
    bill += 15  
elif size =="M":
    bill += 20
elif size =="L":
    bill += 25
else:
    print("you typed the wrong input.")
#todo:work out how much to add to their bill based on their pepperoni choice.
if pepperoni =="Y":
    if size =="S":
        bill += 2
    else:
        bill += 3
#todo:work out their final amount based on weather if they want extra cheese.
if extra_cheese =="Y":
    bill +=1

print(f"your final bill is:${bill}.")
 