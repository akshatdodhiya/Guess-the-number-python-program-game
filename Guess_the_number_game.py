#Program Developed by Akshat Dodhiya
from random import random

n = int(random()*10)
print(n)
tries = 3
guess = 1
print("This game is made by ~ Akshat Dodhiya")
print("About this game :\n"
      "1.You have to guess the numbers between 0 to 10.\n"
      "2.You will get three tries to guess the number.\n")
while(True):

    if(tries==0):
        print("\n!! GAME OVER !! :( \n")
        break

    print("You have ", tries, " tries left !!\n")
    inp = int(input("Guess the number between 0 to 10\n"))

    if(inp>n):
        print("\nYour number is too big guess smaller number\n")
        tries = tries - 1
        guess = guess + 1
        continue
    elif(inp<n):
        print("\nYour number is too small guess bigger number\n")
        tries = tries - 1
        guess = guess + 1
        continue
    else:
        print("\nCongratulations you have guessed correct number :)\n")
        print("\nYou took ",guess," guesses to finish !! ^_^")
        tries = tries - 1
        break


