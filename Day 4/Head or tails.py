#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random
print("Program for Heads or Tails randomized")
print("Whenever this program runs it gives a random result each and every time")

random_num=random.randint(0,1)
if random_num==0:
    print("Tails")
else:
    print("Heads")
    