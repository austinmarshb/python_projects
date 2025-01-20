# bring in artwork
import art
print(art.logo)

# do the basic calculations
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

# main loop of program
def calculator():
    keep_going = True
    n1 = float(input("-What is the first number?"))

    while keep_going == True:
        for item in operations:
            print(item)
        operator = input("--Choose an operation above.")
        #                  "+\n"
        #                  "-\n"
        #                  "*\n"
        #                  "/\n")
        # reminder for dictionary data pull - print(operations["*"](4,8))
        n2 = float(input("---What is the second number?"))
        answer = (operations[operator](n1, n2))
        print(f"{n1} {operator} {n2} = {answer}!")
        choice = input(f"Type 'Y' to continue calculating with {answer}, or type 'N' to start a new calculation").lower()

        if choice == 'y':
            n1 = answer
        else:
            keep_going = False
            print(art.logo)
            calculator()
            
# inefficient first pass
# if operator == "+":
#     # add(first_number, second_number)
#     prin t(operations["+"](n1, n2))
# elif operator == "-":
#     # subtract(first_number, second_number)
#     print(operations["-"](n1, n2))
# elif operator == "*":
#     # multiply(first_number, second_number)
#     print(operations["*"](n1, n2))
# elif operator == "/":
#     # divide(first_number, second_number)
#     print(operations["/"](n1, n2))

