import random

random_number = int(random.randint(1,10))  # numbers 1 - 10
guess = None
# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

while True:
  guess = input("Take a guess between 1 - 10: ")
  guess = int(guess)
  if guess < random_number:
    print("Too low, guess again: ")
  elif guess > random_number: 
    print("Too high, guess again: ")
  else: 
      print("You guessed right! ")
      play_again = input("Do you want to play again: (y/n)?")
      if play_again == "y":
        random_number = int(random.randint(1,10))  # numbers 1 - 10
        guess = None
      else:
        print("Thank you for playing")
        break

# BONUS - let player play again if they want!