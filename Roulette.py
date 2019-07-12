import random

myInput = input("red, black")
computerInput = random.randint(1,2)

if computerInput == 1:
  computerSelection = "red"
elif computerInput == 2:
  computerSelection = "black"

if computerSelection == myInput:
  print("You win!")
else:
  print("You lose")
