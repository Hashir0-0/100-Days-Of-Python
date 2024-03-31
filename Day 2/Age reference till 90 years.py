# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age=int(age)
days=age*365
weeks=age*52
months=age*12

days_left=90*365-days
weeks_left=90*52-weeks
months_left=90*12-months

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")