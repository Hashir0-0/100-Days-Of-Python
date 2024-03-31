print("Welcome to the tip calculator")
total_bill=float(input("What was the total bill? $"))
tip_per=int(input("What percentage of tip would you like to give? 10, 12, or 15?"))
splitting=int(input("How many people are splitting the bill? "))

tip_added=total_bill*tip_per/100
bill=tip_added+total_bill
individual_bill=round(bill/splitting,2)

print(f"Each person should pay: {individual_bill}")