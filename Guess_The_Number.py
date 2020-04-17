import random
import time

random_number = random.randint(1, 20)
print("What is your name?")
myName = input()
print("Hello, " + myName + ".")

guess_number = ""
guess_limit = 2
guess_count = 0
out_of_guesses = False

while guess_number != random_number and not(out_of_guesses):
    if guess_count <= guess_limit:
        guess_number = int(input("Guess a number: "))
        guess_count += 1
        if guess_number < random_number:
            print("Guess a bigger number.")
        elif guess_number > random_number:
            print("Guess smaller number.")
        elif guess_number == random_number:
            print("You Won! This game will end in 5 seconds.")
            time.sleep(5)
    else:
        out_of_guesses = True
        break

if out_of_guesses:
    print("You're out of guesses. You Lose!")




