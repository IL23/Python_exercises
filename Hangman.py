import random

words = ["winter", "snowman", "skating", "temperature"]
guessCount = 6
playGame = True

while playGame:
    print("Enter 1 to play hangman, 2 to add new word, 3 to quit the program")
    action = input("Enter number: ")
    if not action.isdigit():
        print("Wrong input!")
    elif int(action) == 1:
        word = str(random.choice(words))
        guessedLetters = []
        wrongGuess = 0
        head = "    |"
        arms = "    |"
        legs = "    |"
        while True:
            print("+---+")
            print(" |  |")
            if wrongGuess == 1:
                head = " O  |"
            elif wrongGuess == 2:
                arms = "/   |"
            elif wrongGuess == 3:
                arms = "/|  |"
            elif wrongGuess == 4:
                arms = "/|\ |"
            elif wrongGuess == 5:
                legs = "/   |"
            elif wrongGuess == 6:
                legs = "/ \ |"
            print(head)
            print(arms)
            print(legs)
            print("=========")
            print(f"Guessed letters: {guessedLetters}")
            guessedWord = []
            for i in word:
                if i in guessedLetters:
                    guessedWord.append(i)
                else:
                    guessedWord.append("_ ")
            print("".join(guessedWord))
            if word == "".join(guessedWord):
                print("You win!")
                break
            if wrongGuess == guessCount:
                print(f"The word: {word} \n")
                print("You lose! \n")
                break
            userGuess = input("Enter letter: ").lower()
            guessedLetters.append(userGuess)
            if userGuess not in word:
                wrongGuess += 1
    elif int(action) == 2:
        newWord = input("Enter new word: ").lower()
        words.append(newWord)
        print(f"Added {newWord}")
        print(words)
    elif int(action) == 3:
        print("Quit program! ")
        playGame = False
    else:
        print("Wrong input!")



