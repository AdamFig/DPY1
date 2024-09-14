from datetime import date
import datetime
import math
import random
import os
os.system("clear")

print("Wake up")
print("Brush your teeth")
print("Eat breakfast")

weather = str(input("Is the weather sunny, rainy or snowy?"))

if weather == "sunny":
    print("Wear sunglasses.")
else:
    print("Don't wear sunglasses.")


for i in range(0, 6):
    print(i)

number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number from 1 to 10: "))
    if guess == number:
        print("You guessed the number!")
        break
    elif guess > number:
        print("You guessed too high.")
    else:
        print("You guessed too low")
while True:
    action = int(input(
        "Please select a task: '1. Add two numbers', '2. Display today's date', '3. Exit': "))

    match (action):
        case 1:
            print("Which number do you want to add?")
            number1 = int(input("Please provide the 1st number: "))
            number2 = int(input("Please provide the 2nd number: "))
            print(number1 + number2)
        case 2:
            today = date.today()
            print(f"Today is {today}!")
        case 3:
            break
