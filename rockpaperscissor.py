import random

options = ("rock","paper","scissor")
run = True

while run:
    player = input("Enter a choice(rock,paper,scissor) : ")
    computer = random.choice(options)

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player==computer:
        print("It's a TIE!!")
    elif player=="rock" and computer=="scissor":
        print(f"You Win!, {player} beats {computer}")
    elif player=="paper" and computer=="rock":
        print(f"You Win!, {player} beats {computer}")
    elif player=="scissor" and computer=="paper":
        print(f"You Win!, {player} beats {computer}")
    else:
        print(f"You Lose!, {computer} beats {player}")

    if not input("Play again(Y/N?) :").lower() == "y":
        run = False

        print("***THANKS FOR PLAYING***")    

