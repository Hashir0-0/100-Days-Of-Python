# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name=name1+name2
lower_name=lower_name.lower()

a=lower_name.count('t')
b=lower_name.count('r')
c=lower_name.count('u')
d=lower_name.count('e')

f=lower_name.count('l')
g=lower_name.count('o')
h=lower_name.count('v')
i=lower_name.count('e')

sum1=(a+b+c+d)*10
sum2=f+g+h+i
totalsum=sum1+sum2

if totalsum>=90 or totalsum<=10:
    print(f"Your score is {totalsum}, you go together like coke and mentos.") 
elif totalsum>=40 or totalsum<=50:
    print(f"Your score is {totalsum}, you are alright together.")
else:
    print(f"Your score is {totalsum}.")