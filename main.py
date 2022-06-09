import random

while True:
    choices = ["R", "P", "S"]
    computer =random.choice(choices)
    player = None

    while player not in choices:
        player = input("Pick an option from 'R', 'P', 'S' ")

        if player not in choices:
            print("Invalid choice")

        if player == computer:
            print("Computer:", computer)
            print("Player:", player)
            print("It's a tie")

        elif player =="R":
            if computer =="P":
                print("Computer:", computer)
                print("Player:", player)
                print("You lose!")
            if computer =="S":
                print("Computer:", computer)
                print("Player:", player)
                print("You win!")
            if computer =="R":
                print("Computer:", computer)
                print("Player:", player)
                print("It's a tie!")

        elif player =="P":
            if computer =="P":
                print("Computer:", computer)
                print("Player:", player)
                print("It's a tie!")
            if computer =="S":
                print("Computer:", computer)
                print("Player:", player)
                print("You lose!")
            if computer =="R":
                print("Computer:", computer)
                print("Player:",player)
                print("You win!")

        elif player =="S":
            if computer =="P":
                print("Computer:", computer)
                print("Player:", player)
                print("You win!")
            if computer =="S":
                print("Computer:", computer)
                print("Player:", player)
                print("It's a tie!")
            if computer =="R":
                print("Computer:", computer)
                print("Player:", player)
                print("You lose!")
                

