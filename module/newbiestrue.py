def testVowel():
   x = randint(0,5)
    guess = "Z"
    vowels = ('A','E','I','O','U')



    while guess.capitalize() != vowls[x]:
        guess = input("Pick your Vowl: ")
        if guess.capitalize() != vowls[x]:
            print("WRONG!, try again")
        else:
            print("CORRECT!, you have won the game")