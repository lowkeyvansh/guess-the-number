import random

def guess_number():
    number = random.randint(1, 100)
    guess = int(input("Guess the number: "))
    if guess == number:
        return "You guessed it!"
    elif guess < number:
        return "Too low!"
    else:
        return "Too high!"

print(guess_number())
