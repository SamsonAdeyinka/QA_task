animal_1 = int(input("Enter a number: "))
animal_2 = int(input("enter a second number: "))
option = input("true or false?: ")

if option == "true":
    if animal_1 == 0 and animal_2 > 0:
        print(animal_2)
    elif animal_2 == 0 and animal_1 > 0:
        print(animal_1)
    else:
        print(animal_1 + animal_2)
        
elif option == "false":
    if animal_1 == 0 and animal_2 != 0:
        print(animal_2)
    elif animal_2 == 0 and animal_1 > 0:
        print(animal_1)
    else:
        print(animal_1 * animal_2)

