import random

while True:
    choices = ["r", "p", "s"]
    computer =random.choice(choices)
    player = None

    while player not in choices:
        player = input("Pick an option from 'r', 'p', 's' ")

        if player not in choices:
            print("Invalid choice")

        elif player =="r":
            if computer =="p":
                print("Computer:", computer)
                print("Player:", player)
                print("You lose!")
            if computer =="s":
                print("Computer:", computer)
                print("Player:", player)
                print("You win!")

        elif player =="p":
            if computer =="s":
                print("Computer:", computer)
                print("Player:", player)
                print("You lose!")
            if computer =="r":
                print("Computer:", computer)
                print("Player:",player)
                print("You win!")

        elif player =="s":
            if computer =="p":
                print("Computer:", computer)
                print("Player:", player)
                print("You win!")
            if computer =="r":
                print("Computer:", computer)
                print("Player:", player)
                print("You lose!")

    if player == computer:
            print("Computer:", computer)
            print("Player:", player)
            print("It's a tie")
            continue

    end_game = input("Do you wish to continue playing? (yes/no)")
    if end_game == "no":
        break

