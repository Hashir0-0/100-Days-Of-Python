# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_in_int=int(weight)
height_in_float=float(height)
bmi=weight_in_int//height_in_float**2
bmi_in_int=int(bmi)
print('The BMI is =',bmi_in_int)
