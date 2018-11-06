
import datetime

user = "y"

while (user == "y"):
    print("1.Add\n2.Minus\n3.Multiply\n4.Divide")
    
    try:
        choice = input("What would you like to do? ")
        int(choice)
    except:
        print(choice, " is not the correct format")
        break

    number1 = float(input("What's your first number? "))
    number2 = float(input("What's your second number? "))

    if choice == 1:
        answer = (number1 + number2)
        print(number1,"+",number2,"=",answer)
    if choice == 2:
        answer = (number1 - number2)
        print(number1,"-",number2,"=",answer)
    if choice == 3:
        answer = (number1 * number2)
        print(number1,"*",number2,"=",answer)
    if choice == 4:
        answer = float(number1 / number2)
        print(number1,"/",number2,"=",answer)

    user = raw_input("Would you like a new calculation? y/n ")
