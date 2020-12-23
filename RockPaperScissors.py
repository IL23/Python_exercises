# Izveidot spēli “Akmens šķēres papīrīt’s”.

import random

pointsPC = 0
pointsUser = 0
figures = ("Rock", "Paper", "Scissors")
winner = "Nobody"

while pointsPC < 3 and pointsUser < 3:
    figurePC = random.randint(1, 3)
    print("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ")
    figureUser = int(input("Your turn: "))

    if 1 <= figureUser <= 3:
        if figureUser == figurePC:
            winner = ""
        elif (figureUser - figurePC == 1) or (figurePC == 3 and figureUser == 1):
            pointsUser += 1
            winner = "User"
        else:
            pointsPC += 1
            winner = "Computer"

        print(f"{figures[figureUser-1]} vs. {figures[figurePC-1]}")
        print("Draw") if figurePC == figureUser else print(f"{winner} wins this round.")
        print(f"{pointsUser}:{pointsPC}\n")
    else:
        print("Wrong input. Try again! \n")

print(f"{winner} wins! ")

