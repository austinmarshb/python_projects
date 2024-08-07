print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")

if size in ["S", "M", "L"]:
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni in ["Y", "N"]:
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese in ["Y", "N"]:
            price = 0

            if size == "S":
                price = 15
            elif size == "M":
                price = 20
            elif size == "L":
                price = 25

            if size == "S" and pepperoni == "Y":
                price += 2
            elif size != "S" and pepperoni == "Y":
                price += 3

            if extra_cheese == "Y":
                price += 1

            print(f"Your final bill is ${price}.")
        else:
            print("You did not select a valid option for extra cheese.")
    else:
        print("You did not select a valid option for pepperoni.")
else:
    print("You did not select a valid size.")
