import re


# Introduction to the Game

#code for if they put more than three words


HANGMANVISUALS= ["""
        _______
        |     |
        |     
        |
        |
        |
        |
        |________
        |        |
        """, """
        _______
        |     |
        |     Ofile:/Users/marisleysisdelacruz/PycharmProjects/105project-delacruz-kalombo-green/hangman.py
        |     
        |
        |
        |
        |________
        |        |
        """ , """
        _______
        |     |
        |     O
        |     |
        |
        |
        |
        |________
        |        |
        """, """
        _______
        |     |
        |     O
        |   --|
        |     
        |    
        |
        |________
        |        |
        """, """
        _______
        |     |
        |     O
        |   --|--
        |     
        |     
        |
        |________
        |        |
        """, """
        _______
        |     |
        |     O
        |   --|--
        |    / 
        |     
        |
        |________
        |        |
        """, """
        _______
        |     |
        |     O
        |   --|--
        |    / \ 
        |     
        |
        |________
        |        |
        """, ]
#these are the visuals for the game

def startUp():
   print ("This is the hangman game with a plot twist called Word Catcher. \n")
   print ("These are the rules of the game and they apply to both players when the roles are reversed. \n")
   print ("This game will go on for 6 rounds. \n")
   print ("After each round the players that starts first alternates. Player 1 starts round 1. \n")
   print ("Player 1 will enter a 3 word phrase to be guessed by player 2. \n")
   print ("Player 2 then has to guess one letter at a time until he/she has guessed \n")
   print ("all of the letters in the phrase or has run out of chances. \n")
   print ("The player has to guess the phrase using at most 6 chances. \n")
   print ("If player 2 guesses the phrase then it gets added into their word bank. \n")
   print ("If player 2 doesn't guess the word then it's added into player 1's word bank. \n")
   print ("At the end of the 6 rounds, the player with the most words in their word bank wins. \n")

   main()


correctletters = ""  # correctletters stores the letters correctly guessed by the player
incorrectletters = ""  # incorrectletters stores the letters incorrectly guessed by the player
remainingChances = 6
player1wordbank = []
player2wordbank = []

def main(): #this is the sequence in which the game will run in

    global player1wordbank #made the word banks global so we can change them within the function
    global player2wordbank
    global incorrectletters
    global correctletters
    global remainingChances

    guesser = True  # true when player 1 is guessing, false when player 2 is guessing

    print("************************************************************")
    print(" \n Starting a new game of Word Catcher \n")
    print(HANGMANVISUALS[0])
    print("************************************************************ \n")

    # with each less chance, a hangman is drawn and when the drawing is complete the game is over

    for i in range(6): #this makes the game loop for six rounds
        input_word, gameWord = inputword()  #creates parameters for the function inputword

        while remainingChances != 0 and gameWord.find('_') != -1:  # Check if all the letters have been guessed
            gameWord = guessword(input_word, gameWord)
            print(gameWord)

        if remainingChances == 0: #This is when the guessing player loses the round by running out of chances
            lostRound(input_word)
        else:
            print("You have guessed the phrase correctly. This word is in your word bank.")
            if guesser == True:
                player1wordbank.append(gameWord) #this when player 1 correctly guesses the word
                print ("Player 1's Word Bank: " + str(player1wordbank))
                print ("Player 2's Word Bank: " + str(player2wordbank))
                print("It is now player 2's turn.")
            else:
                player2wordbank.append(gameWord)
                print("Player 1's Word Bank: " + str(player1wordbank))
                print("Player 2's Word Bank: " + str(player2wordbank))
                print("It is now player 1's turn.")
        guesser = not guesser  #this allows the players to switch roles between guessing and giving the word
        correctletters = ""  # resets the correct letters for player 2
        incorrectletters = ""  # resets the correct letters for player 1
        remainingChances = 6 #resets the remaining guesses the player has for new round

   # checks the length of player1 word bank vs length of player 2 wordbank
    if len(player1wordbank) > len(player2wordbank):
        print("Player 1's Word Bank: " + str(player1wordbank))
        print("Player 2's Word Bank: " + str(player2wordbank))
        print("Player 1 wins!")
    if len(player1wordbank) < len(player2wordbank):
        print("Player 1's Word Bank: " + str(player1wordbank))
        print("Player 2's Word Bank: " + str(player2wordbank))
        print("Player 2 wins!")
    if len(player1wordbank) == len(player2wordbank):
        print("Player 1's Word Bank: " + str(player1wordbank))
        print("Player 2's Word Bank: " + str(player2wordbank))
        print("It's a tie!")

   # if the word is fully guessed, then it will add the word to the word bank


def inputword():
    input_word = input("Please enter phrase to guess: \n ") #this is instructions for the wordgiving player
    gameWord = ""

    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  # online source: Geeksforgeeks

    while (regex.search(input_word) != None):  #this makes sure that the word given doesnt have special characters
       print("String is not accepted. \n Try again.")
       input_word = input("Please enter phrase to guess: ")  #this makes the wordgiving player try again

    for i in input_word:
        if i != ' ' and i != '-' and i != "'":
            gameWord += "_ " #this prints underscores to hide each letter of the given word
        else:
            gameWord += i + " "
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    return input_word, gameWord


def guessword(input_word, gameWord):
    guess_word = ""
    global incorrectletters #made the letter and chances global so we can change them within the function
    global correctletters
    global remainingChances
    while True:
       # Asks the user for a guess
        guess_word = input("\nYour guess (letters only): ")

       # only letters are allowed and check if the letter has already been guessed.
        if not guess_word.isalpha():
            print("Not a valid character. Please enter a letter.")
        elif guess_word.lower() in incorrectletters or guess_word.lower() in correctletters:
            print("You have already tried this letter or digit. \n Guess again!")
        else:
            break

   # Check if the letter/digit is present in the name to be guessed.
   # If yes, add it to the correctletters.
    if guess_word.lower() not in input_word.lower():
        incorrectletters += guess_word.lower()
        print("This letter is not present in the phrase.")
        remainingChances -= 1 # this means the guessing player has one less chance to guess the word
        if remainingChances == 6:
            print(HANGMANVISUALS[0])

        elif remainingChances == 5:
            print(HANGMANVISUALS[1])

        elif remainingChances == 4:
            print(HANGMANVISUALS[2])

        elif remainingChances == 3:
            print(HANGMANVISUALS[3])

        elif remainingChances == 2:
            print(HANGMANVISUALS[4])

        elif remainingChances == 1:
            print(HANGMANVISUALS[5])

        elif remainingChances == 0:
            print(HANGMANVISUALS[6])
        print("Chances Remaining   : ", remainingChances)
        print("Missed Letters : ")
        if not len(incorrectletters):
            print("None")
        else:
            print(incorrectletters)
    else:
        correctletters += guess_word.lower()
        n = input_word.lower().find(guess_word.lower())
        while n != -1:
            gameWord = gameWord[0:n * 2] + input_word[n] + ' ' + gameWord[n * 2 + 2:]
           # this replaces the underscore with the correct letter guessed
            n = input_word.lower().find(guess_word.lower(), n + 1)

    return gameWord


def lostRound(input_word):
    print("You have lost the game.")
    print("The phrase was: ")
    for i in input_word:  # this will print the word given by the wordgiving player
        print(i)


def endGame():  # asks the user if they want to play again, if yes then it restarts if not then the game ends
   print ("******************************")
   restartGame = input("Do you wish to play again? (yes/no):")
   restartGame = restartGame.lower()  # makes the input lowercase in case the user inputs a capital word
   if restartGame == "yes":  # restarts the game if the user wants to play again
       print ("")
       print ("")
       startUp()  # restarts the game


# Mainline
startUp()
