# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Method 1
n=len(names)
rand_num=random.randint(0,n-1)
random_name=names[rand_num]
print(f"{random_name} Will pay the bill today.")

#Method 2
rand_name=random.choice(names)
print(f"{rand_name} Will pay the bill today.")