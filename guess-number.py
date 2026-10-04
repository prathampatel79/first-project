import random

computerNumber = random.randint(1,100)
userGuess = int(input("Enter your Guess bw 1 and 100: "))
userAttempt = 1


while (userGuess != computerNumber):
    if (userGuess < computerNumber):
        print("Guess was a bit LOWER, try again with some number higher than", userGuess)

    else:
 
        print("Guess was a bit HIGHER, try again with some number lower than", userGuess)
    userGuess = int(input("Enter your Guess bw 1 and 100: "))
    userAttempt += 1

print("You guessed it right!! The number was", computerNumber,"\nYou took", userAttempt, "attempt(s)")