from random import randint 

rand_index = randint(0, 2)
choices = ["rock", "paper", "scissors"]
computer = choices[rand_index]
print("Choose: rock, paper, scissors")
player = input("Player, make your move: ")

if player == computer:
  print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("Computer's move: scissors")
        print("player wins!")
    elif computer == "paper":
        print("Computer's move: paper")
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("Computer's move: paper")
        print("player wins!")
    elif computer == "scissors":
        print("Computer's move: scissors")
        print("computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("Computer's move: paper")
        print("player wins!")
    elif computer == "rock":
        print("Computer's move: rock")
        print("computer wins!")  
else:
    print("something went wrong")