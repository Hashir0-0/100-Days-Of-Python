# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Method 1

leap1=year//4
leap2=year//100
leap3=year//400
    
if leap1&leap3%2==0 | leap2%2==0:
    print("Leap Year")
else:
    print("Not leap year")

#Method 2

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not Leap Year.")