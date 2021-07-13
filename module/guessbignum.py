from random import randint
import newbies

x = randint(1,999)
guess = -1

newbies.printplus()

while guess != x:
    guess = int(input("Pick your number: "))
    if guess < x:
        print("Too low, try again")
    elif guess > x:
        print("Too high, try again")
    else:
        print("CORRECT!, you have won the game")
