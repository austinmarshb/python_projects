 # from art import logo, vs
 # from game_data import data
 # import random


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


game_on = True

print(logo)
while game_on:
    choice_a = random.choice(data)
    choice_b = random.choice(data)
    print(f"Compare CHOICE A: {format_data(choice_a)}.")
    print(vs)
    print(f"Compare CHOICE B: {format_data(choice_b)}.")
    user_choice = input("Who has more instagram followers? Type 'A' or 'B'\n").lower()
    if user_choice == 'a' and choice_a["follower_count"] > choice_b["follower_count"]:
        print("You got it! Here's another...")
    elif user_choice == 'b' and choice_b["follower_count"] > choice_a["follower_count"]:
        print("You got it! Here's another...")
    else:
        print("Sorry, wrong answer!")
        game_on = False
