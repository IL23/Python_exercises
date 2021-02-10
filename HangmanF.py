import random

words = ["winter", "snowman", "skating", "temperature"]
guessCount = 6
playGame = True


def make_guessed_word(right_word, guessed_letters_list):
    word_guessed = []
    for i in right_word:
        if i in guessed_letters_list:
            word_guessed.append(i)
        else:
            word_guessed.append("-")
    return "".join(word_guessed)


def add_new_word(words_list):
    new_word = input("Enter new word: ").lower()
    if new_word not in words_list:
        words_list.append(new_word)
    print(f"Added {new_word}")
    return words_list


def draw_hangman(wrong_guesses):
    head = "    |"
    arms = "    |"
    legs = "    |"
    if wrong_guesses >= 1:
        head = " O  |"
    if wrong_guesses == 2:
        arms = "/   |"
    elif wrong_guesses == 3:
        arms = "/|  |"
    elif wrong_guesses >= 4:
        arms = "/|\ |"
    if wrong_guesses == 5:
        legs = "/   |"
    elif wrong_guesses == 6:
        legs = "/ \ |"
    print("+---+")
    print(" |  |")
    print(f"{head}\n{arms}\n{legs}")
    print("    |")
    print("=========")


while playGame:
    print("Enter 1 to play hangman, 2 to add new word, 3 to quit the program")
    action = input("Enter number: ")
    if not action.isdigit():
        print("Wrong input!")
    elif int(action) == 1:
        word = str(random.choice(words))
        guessedLetters = []
        wrongGuess = 0
        while True:
            guessed_word = make_guessed_word(word, guessedLetters)

            if word == guessed_word:
                print(word)
                print("You win!")
                break

            draw_hangman(wrongGuess)

            if wrongGuess == guessCount:
                print(word)
                print("You lose! \n")
                break

            print(f"Guessed letters: {', '.join(guessedLetters)}")

            print(guessed_word)

            user_guess = input("Enter letter: ").lower()
            guessedLetters.append(user_guess)

            if user_guess not in word:
                wrongGuess += 1

    elif int(action) == 2:
        words = add_new_word(words)
    elif int(action) == 3:
        playGame = False
    else:
        print("Wrong input!")





