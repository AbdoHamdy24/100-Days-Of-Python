import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images = [rock, paper, scissors]
user_choice = input("What do you choose? type 0 for rock, 1 for paper or 2 for scissors.\n")

if int(user_choice) <= 2 and int(user_choice) >= 0 :
    print(images[int(user_choice)])
else:
    print("Incorrect Answer!")    

print("Computer Choice:")    
computer_choice = random.randint(0,2)
print(images[computer_choice])

if computer_choice == int(user_choice):
    print("Draw!")
elif computer_choice == 2 and int(user_choice) == 1:
    print("You lose!")
elif computer_choice == 2 and int(user_choice) == 0:
    print("You win!")        
elif computer_choice == 0 and int(user_choice) == 1:
    print("You win!")
elif computer_choice == 0 and int(user_choice) == 2:
    print("You lose!")
else:
    print("Incorrect Answer, You lose!")    

