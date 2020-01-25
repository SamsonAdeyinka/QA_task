cont = True

while cont == True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("NUMBER PLEASE!!!")
        
    number2 = int(input("Enter another number: "))
    operator = input("Operator: ")
    
    if operator == "+":
        answer = number + number2
        print(answer)
    elif operator == "-":
        answer = number - number2
        print(answer)
    elif operator == "*":
        answer = number * number2
        print(answer)
    elif operator == "/":
        answer = number / number2
        print(answer)

    move = input("Would you like to continue using the calculator?: ")
    move.lower
    if move == "no" or move == "n":
        cont = False
        print("Finished")
    elif move == "yes" or move == "y":
        cont

