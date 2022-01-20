# Classic Rock-Paper-Scissors but in as few lines as I can do. #
import random
choices = ["rock", "paper", "scissors"]
player = computer = None
repeat = True
while repeat == True:
   win = False
   while win == False:
      computer = random.choice(choices)
      player = (input("[Rock, Paper, or Scissors]: ").lower())
      print("Computer: " + computer + "\nPlayer: " + player)
      if(player in choices):
         if player == computer:
            print(("Tie Game!").upper())
         else:
            if (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
               print((player + " beats " + computer + "!\nPlayer Wins!").upper())
            else:
               print((computer + " beats " + player + "!\nComputer Wins!").upper())
         win = True
   repeat = ((input("Play Again? [y,n] ").lower()) == "y")