import random

# function to pick a random number between 1 and 10
def chooseRandomNumber():
    number = random.randint(1, 10)
    return number

def main():
    # set the computer's number
    number = chooseRandomNumber()
    # user guess
    guess = input("Please guess a number between 1 and 10.")
    # boolean to control the while loop
    correct = False

    while not correct:

        try:
            if int(guess) == number: # correct guess - end the loop
                correct = True
                print("Congratulations! You guessed the number correctly.")
            elif int(guess) < 1 or int(guess) > 10: # make sure the guess is within range
                guess = input("Your number is not between 1 and 10, guess again.")
            elif int(guess) < number:
                guess = input("Too low, guess a higher number.")
            elif int(guess) > number:
                guess = input("Too high, guess a lower number.")
            else:
                guess = input("Hmmm, there was an error. Guess again.")

        except ValueError: # if the user entered letters or invalid characters
            guess = input("This is not a valid entry, guess again.")

main()