#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  playAgain = "Y"
while playAgain == "Y":
  #User can play as many games as they wish.
  #Randomly choose the computer between 'R', 'P', 'S'
  computer = random.choice(["R","P", "S"])
  #Prompt the user for their RPS selection
  player = input("Pick your fighter (R, P, S)")
  #Determine winner and state what happened to the user
  if computer == "R":
    print("computer chose Rock")
  elif computer == "P":   
    print("computer chose paper")
  else:
    print("player chose scissors")  
  if player == "R":
    print("player chose Rock")
  elif player == "P":   
    print("computer chose paper")
  else:
    print("player chose scissors")  
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)
if player == "R" and computer == "R":
  print("Tie")
  ties = ties + 1
if player == "R" and computer == "P":
  print("Computer wins.")
  losses = losses + 1
if player == "R" and computer == "S":
   print("You win!")
   wins = wins + 1
 if player == "S" and computer == "S":
  print(Tie)
  ties = ties + 1
if player == "S" and computer == "R":
  print("Computer wins.")
  loses = loses + 1
if player == "S" and computer == "P":
   print("You win!")
   wins = wins + 1       
 if player == "P" and computer == "P":
  print(Tie)
  ties = ties + 1
if player == "P" and computer == "S":
  print("Computer wins.")
  loses = loses + 1
if player == "P" and computer == "R":
   print("You win!")
   wins = wins + 1  
# Ask user if they want to play again
playAgain = input("Play again? (Y/N):")   
if __name__ == '__main__':
  main()
