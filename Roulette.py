import random

keepplaying = True  
while keepplaying == True:
  myInput = input("Bet your color Type: Red or Black:")
  myInput = myInput.lower()
  computerInput = random.randint(1,2)
  
  if computerInput == 1:
    computerSelection = "red"
  elif computerInput == 2:
    computerSelection = "black"
  
  if computerSelection == myInput:
    print("You win!")
  else:
    print("You lose")
    
  user_input = input("Do you want to continue playing?")
  if user_input == "no":
    keepplaying = False
