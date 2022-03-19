import random

def multGame(n1, n2):
    n3 = n1*n2
    return n3

def divGame(n1, n2):
    if n2 == 0:
        print("Divide by zero")
        
    n3 = n1//n2
    return n3

def addGame(n1, n2):
    n3 = n1+n2
    return n3

def subGame(n1, n2):
    n3 = n1-n2
    return n3

def basicOperatorsGame(n1, n2, operatorType):
    if operatorType == 1:
        answer = addGame(n1,n2)
        print("What is", randNum1, "+", randNum2,"?")
    elif operatorType == 2:
        answer = subGame(n1,n2)
        print("What is", randNum1, "-", randNum2,"?")
    elif operatorType == 3:
        answer = multGame(n1,n2)
        print("What is", randNum1, "*", randNum2,"?")
    elif operatorType == 4:
        while n2 == 0:
            n2 = random.randint(range1, range2)
        answer = divGame(n1,n2)
        print("What is", randNum1, "//", n2,"?")
    return answer

def modulusGame(n1, n2):
    n3 = n1%n2
    return n3

def get_int_between_x_and_y_inclusive(prompt, x, y):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < x or value > y:
            print("Enter a value from", x, "to", y,".")
            continue
        else:
            break
    return value

def get_greater_than_zero_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 1:
            print("Enter a value greater than zero.")
            continue
        else:
            break
    return value

def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a number")
            continue

        else:
            break
    return value

def get_valid_range(prompt,range):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a number")
            continue

        if value < range:
            print("Enter a valid range.")
            continue
        else:
            break
    return value

while True:

    print("This is a Calculator Math Game!")
    print("The goal of this game is practice basic and advanced math functions")
    print()
    print("Type the games number to select that game")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Floor Division")
    print("5. Basic operators with floor division")
    print("6. Modulus")
    chosengame = get_int_between_x_and_y_inclusive("",1,6)
    print()
    
    print("What range of numbers do you want to use?")
    range1 = get_valid_int("Enter the lower end of the range: ")
    range2 = get_valid_range("Enter the higher end of the range: ",range1)
    print()

    
    questionAmount = get_greater_than_zero_int("How many questions do you want to be asked?: ")
    print()
    print()
    score = 0

    for i in range(questionAmount):
        randNum1 = random.randint(range1, range2)
        randNum2 = random.randint(range1, range2)

        if chosengame == 1:
            answer = addGame(randNum1,randNum2)
            print("What is", randNum1, "+", randNum2,"?")

        elif chosengame == 2:
            answer = subGame(randNum1,randNum2)
            print("What is", randNum1, "-", randNum2,"?")

        elif chosengame == 3:
            answer = multGame(randNum1,randNum2)
            print("What is", randNum1, "*", randNum2,"?")

        elif chosengame == 4:
            while randNum2 == 0:
                randNum2 = random.randint(range1, range2)
            answer = divGame(randNum1,randNum2)
            print("What is", randNum1, "//", randNum2,"?")

        elif chosengame == 5:
            operatorType = random.randint(1,4)
            answer = basicOperatorsGame(randNum1,randNum2,operatorType)

        elif chosengame == 6:
            while randNum2 == 0:
                randNum2 = random.randint(range1, range2)
            answer = modulusGame(randNum1,randNum2)
            print("What is", randNum1, "%", randNum2,"?")


        while True:
            try:
                if float(input()) == answer:
                    print("Correct!")
                    score = score + 1
                    print()

                else:
                    print("Incorrect!")
                    print("The Answer was", answer, "!")
                    print()

            except ValueError:
                print("Please enter a number.")
                continue
            else:
                break



    print("Your score was",score,"out of",questionAmount)
    print("Would you like to play again?")
    print("1. Yes")
    print("2. No")
    print()
    choice = get_int_between_x_and_y_inclusive("",1,2)
    if choice == 2:
        break

