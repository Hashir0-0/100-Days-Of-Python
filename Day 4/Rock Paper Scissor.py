rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choices=[rock,paper,scissors]

comp_choice=random.choice(choices)

human_choice=int(input("What do you choose? Type 0 for Rock,1 for Paper,2 for Scissors."))

if human_choice==0:
    print(rock)
elif human_choice==1:
    print(paper)
elif human_choice==2:
    print(scissors)
else:
    print("Sorry invalid input")

print(comp_choice)

if human_choice==1 and comp_choice==rock:
    print("You win")
elif human_choice==2 and comp_choice==paper:
    print("You win")
elif human_choice==0 and comp_choice==scissors:
    print("You win")
else:
    print("You lose")
