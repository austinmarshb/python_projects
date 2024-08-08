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

#import modules
import random

#art array
game_art = [rock, paper, scissors]

#define variables
user_choice = int(input("Choose One: Type 0 for Rock, 1 for Paper, 2 for Scissors"))
computer_choice = random.randint(0,2)

#print result
if user_choice <= 2:
    user_art_choice = game_art[user_choice]
    computer_art_choice = game_art[computer_choice]
    print(f"You chose: {user_art_choice}")
    print(f"Computer chose: {computer_art_choice}")

#rules
if user_choice >= 3 or user_choice < 0:
    print("You did not choose a valid input.")
elif user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif computer_choice == 2 and user_choice == 0:
    print("You Win!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
