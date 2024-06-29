print("Welcome to the rollercoaster")
height=int(input("Please enter your height in cm :"))
bill=0
if height>=120:
    print("You are allowed to enter the rollercoaster!")
    age=int(input("What is your age?"))
    if age <12:
        bill=5
        print("Child ticket is 5$")
    elif age<=18:
        bill=7
        print("Youth ticket is 7$")
    elif age>=45 and age<=55:
        bill=0
        print("Free tickets for people of midlife crisis")
    else:
        bill=12
        print("Adult ticket is 12$")
    
    take_photos=input("Do you want to take photos ? Y(Yes) or N(No).")
    if take_photos=="Y":
        bill+=3
    
    print(f"Your total bill is {bill}")
    
else:
    print("Sorry you cannot enter the rollercoaster.")