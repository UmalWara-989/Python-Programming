import random

randNumber = random.randint(1,100)
guesses = 0
userGuess = None

while (userGuess != randNumber):
    guesses += 1

    userGuess = int(input("Enter your guess : "))
    if (userGuess==randNumber):
        print("Congratulations! you guessed it right\n")
    elif userGuess > randNumber:
        print("Wrong! Enter smaller number\n")
    else:
        print("Wrong! Enter larger number\n")    

print(f"You guessed the number in '{guesses}' guesses!")

with open("highScore.txt") as f:
    highScore = int(f.read())

if (guesses < highScore):
    print("You have just broken the High Score!")
    with open("highScore.txt","w") as f:
        f.write(str(guesses))

