import os
os.system("clear")
import random

# print("Start")
# print("Process")
# print("End")

# age = 16
# if age >= 18:
#     print("You are old enough to vote!")
# elif age == 17:
#     print("You can vote next year!")
# else:
#     print("You are too young to vote.")

secret_number = random.randint(1, 10)
counter = 0


while True:
    guess = int(input("Please guess the secret number: "))
    counter += 1
    if guess == secret_number:
        print(f"You have guessed the number in {counter} guesses!")
        break
    elif guess > secret_number:
        print("You have guessed too high.")
    else:
        print("You have guessed too low.")
        secret_number = random.randint(1,10)
