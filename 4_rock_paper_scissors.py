# This is a rock, paper, scissors game. It is supposed to showcase the usage of the random module.

# Isso é um jogo de pedra, papel e tesoura. Ele demonstra o uso do módulo random.

import random

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

your_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
if your_choice == 0:
    print(rock)
elif your_choice == 1:
    print(paper)
elif your_choice == 2:
    print(scissors)

print("Computer chose:")
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if your_choice == 0:
    if computer_choice == 0:
        print("That's a draw.")
    elif computer_choice == 1:
        print("You lost.")
    elif computer_choice == 2:
        print("You won.")
elif your_choice == 1:
    if computer_choice == 0:
        print("You won.")
    elif computer_choice == 1:
        print("That's a draw.")
    elif computer_choice == 2:
        print("You lost.")
elif your_choice == 2:
    if computer_choice == 0:
        print("You lost.")
    elif computer_choice == 1:
        print("You won.")
    elif computer_choice == 2:
        print("That's a draw.")
