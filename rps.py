import random

print("Welcome to the Game of Rock, Paper, and Scissors!!")

choices = ("rock", "paper", "scissors")
player = None
rounds_played=0
game=True
while game:
     rounds_played = 0
     while rounds_played < 3:
         player = input("Enter your choice...(rock,paper,scissor)      ").lower()
         while player not in choices:
             print("Invalid choice entered...")
             player = input("Enter your choice...(rock,paper,scissor)      ").lower()
         computer=random.choice(choices).lower()

         if player == computer:
             print("Tie!")
         elif player == 'rock' and computer == 'scissors':
             print("You win!")
         elif player == 'scissors' and computer == 'paper':
             print("You win!")
         elif player == 'paper' and computer == 'rock':
             print("You win!")
         else:
             print("You Lose!")
         rounds_played += 1
     again=input("Would you like to play again?(Y/N)    ")
     if again == 'N':
       print("Thank you for playing, Goodbye!")
       game = False
