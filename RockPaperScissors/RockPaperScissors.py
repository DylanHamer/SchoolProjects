import random

choices = ["rock", "paper", "scissors"]
gameNumber = 0

def rockPaperScissors(mode, gameNumber):
    if mode == "1":
        aiChoice = random.choice(choices)
        chosen = False
        while not chosen:
            playerChoice = input("Please choose: ")
            if playerChoice in choices:
                chosen = True
            else:
                print("Invalid choice!")
                chosen = False

    playerWins = [('scissors', 'paper'), ('paper', 'rock'), ('rock', 'scissors')]
    print("\n------------------------------")
    print("Game number: " + str(gameNumber))
    print("You chose: " + playerChoice)
    print("AI chose: " + aiChoice)
    if (playerChoice, aiChoice) in playerWins:
        print(playerChoice + " beats " + aiChoice)
        print("You win!")
    elif playerChoice == aiChoice:
        print(playerChoice + " does nothing to " + aiChoice)
        print("Draw!")
    else:
        print(aiChoice + " beats " + playerChoice)
        print("You lose!")
    print("------------------------------\n")

while True:
    print("Please choose a mode: ")
    print("1. AI vs Player")
    print("2. AI vs AI")
    print("3. Player vs Player")
    mode = input("Mode? ")

    if mode == "1" or mode == "2" or mode == "3":
        while True:
            gameNumber += 1
            rockPaperScissors(mode, gameNumber)
    else:
        print("Invalid choice!")


    
    
