# Program Developed by Akshat Dodhiya
# Exercise - 3
from random import random

n = int(random() * 10)  # Generating random number
tries = 3  # Initializing the number of tries in the beginning of the game
guess = 1  # Initializing the number of guesses
print("This game is made by ~ Akshat Dodhiya")
print("About this game :\n"
      "1.You have to guess the numbers between 0 to 10.\n"
      "2.You will get three tries to guess the number.\n")  # Printing about of the game
while True:  # An infinite loop to start the game

    if tries == 0:  # Printing statement if the user ran out of chances
        print("\n!! GAME OVER !! :( \n")
        print("The correct number was", n)
        break

    print("You have ", tries, " tries left !!\n")  # Printing number of chances left for the user
    inp = int(input("Guess the number between 0 to 10\n"))  # Taking the input of the user for number

    if inp > n:  # Condition if the guessed number is greater than the number to be guessed
        print("\nYour number is too big guess smaller number\n")
        tries = tries - 1
        guess = guess + 1
        continue
    elif inp < n:  # Condition if the guessed number is smaller than the number to be guessed
        print("\nYour number is too small guess bigger number\n")
        tries = tries - 1
        guess = guess + 1
        continue
    else:  # Condition if the user guesses the correct number
        print("\nCongratulations you have guessed correct number :)\n")
        print("\nYou took ", guess, " guesses to finish !! ^_^")
        tries = tries - 1
        break
