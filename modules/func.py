import random
def whil(ea):
    points = 0
    guesses = 5
    while (guesses > 0):
        num = random.randint(1, ea)
        while (guesses > 0):
            print("Guess the number (1 - %d)" % ea)
            guess = int(input("Guess > "))
            if(num == guess):
                num = random.randint(1, ea)
                print("Correct!")
                points += 1
                guesses = 5
            else:
                print("Oops! You got it wrong. Guess again!")
                guesses -= 1
    print("You lost! With a score of", points)

def startGame(e):
    if(e == 1):
        whil(5)

    elif(e == 2):
        whil(8)

    elif(e == 3):
        whil(12)

    elif(e == 4):
        ea = int(input("> 1 to "))
        whil(ea)