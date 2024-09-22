
def calculator():

    def add(n1, n2):
        return n1 + n2
    def subtract(n1, n2):
        return n1 - n2
    def multiply(n1, n2):
        return n1 * n2
    def division(n1, n2):
        return n1 / n2

    # Adding in a dict | we don't need parenthesis here
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": division
    }

    answer1 = "n"
    while answer1 == "n":
        n1 = float(input("What's the first number? "))
        answer = "y"
        while answer == "y":
            for symbol in operations:
                print(symbol)
            my_favorite_operation = input("Pick an operation: ")

            n2 = float(input("What's the next number? "))

            #Using the dict operations
            if my_favorite_operation == "+":
               new_1 = operations["+"](n1,n2)
               print(f"{n1} + {n2} = {new_1}")
               n1 = new_1
            elif my_favorite_operation == "-":
               new_1 = operations["-"](n1,n2)
               print(f"{n1} - {n2} = {new_1}")
               n1 = new_1
            elif my_favorite_operation == "*":
               new_1 = operations["*"](n1,n2)
               print(f"{n1} * {n2} = {new_1}")
               n1 = new_1
            elif my_favorite_operation == "/":
               new_1 = operations["/"](n1,n2)
               print(f"{n1} / {n2} = {new_1}")
               n1 = new_1
            else:
                 "You must choose one of above operations"

            # Decision for the loop
            answer = input(f"Type 'y' to continue calculating with {n1}, or type 'n' to start a new calculation \n").lower()

            if answer == "y":
                answer = "y"
            elif answer == "n":
                answer = "n"
                answer1 = answer
                print("\n" * 20)
            else:
                break

calculator()