# import art
# import random
# print(art.logo)
# ^ specific to local files not uploaded
print("Welcome to the number guessing games!")
print("I'm thinking of a number between 1 and 100")
user_choice = input("Choose a difficulty: Type 'easy' or 'hard:").lower()

guesses_remaining = int()
game_running = True

if user_choice == 'easy':
    guesses_remaining = 10
    print(f"You have {guesses_remaining} attempts remaining to guess the number")
elif user_choice == 'hard':
    guesses_remaining = 5
    print(f"You have {guesses_remaining} attempts remaining to guess the number")
else:
    input("Invalid inpout. Please choose a difficulty: 'easy or 'hard'")

secret_number = int(random.choice(range(1, 101)))

while game_running:
    user_choice = int(input("Make a guess: "))
    if user_choice == secret_number:
        print(f"You got it! {secret_number} was the number I was thinking of!")
        game_running = False
    elif user_choice < secret_number:
        print("Too low, try again.")
        guesses_remaining -= 1
        print(f"You have {guesses_remaining} attempts left.")
    elif user_choice > secret_number:
        print("Too high, try again.")
        guesses_remaining -= 1
        print(f"You have {guesses_remaining} attempts left.")

    if guesses_remaining == 0:
        print(f"Sorry, you ran out of guesses! I was thinking of the number {secret_number}!")
        game_running = False
