# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight=float(weight)
height=float(height)
bmi= round(weight/height**2,2)
print('The BMI is =',bmi)
if bmi <=18.5:
    print("You are underweight")
elif bmi<25:
    print("You are normal weight")
elif bmi<30:
    print("You are overwight")
elif bmi<35:
    print("You are obese")
elif bmi>35:
    print("You are clinically obese")
    