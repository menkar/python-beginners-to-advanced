import random

randomNum = random.randint(1, 10);
# print(randomNum)
tries = 0

while True:
        
    guessNum = int(input("Guess your number from between 1 to 10 : "))

    if randomNum == guessNum:
        tries += 1
        print(f"you are right you guessed the number is {tries} tries")
        break

    if randomNum == guessNum:
        tries += 1
        print("You are correct")

    elif randomNum < guessNum:
        tries += 1
        print("Go a little lower")

    elif randomNum > guessNum:
        tries += 1
        print("Go a little higher")

    else:
        tries += 1
        print("Sorry, you are wrong")

