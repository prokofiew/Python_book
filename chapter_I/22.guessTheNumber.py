# Whis is a guess the number game
import random
secretNumber = random.randint(1, 20)
print("I am thinking of a numer between 1 and 20.")
#ask the player to guess six times.
for guessesTaken in range (1,7):
    print("Take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("Your guess is to low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break   # THis condition is the correct guess!
if guess == secretNumber:
    print("Good Job! You guessed my number in "+ str(guessesTaken) + " guesses!")
else:
    print("Nope, the number I was thinking of was " + str(secretNumber))
      