import random

# Rules: Each key beats the values in its list
rules = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

choices = list(rules.keys())  # ['rock', 'paper', 'scissors', 'lizard', 'spock']

print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")

# FIRST WHILE LOOP: To keep playing the full game
while True:
    player_score = 0
    computer_score = 0
    rounds = 0

    print("\nLet's start the game!")

    # SECOND WHILE LOOP: Play multiple rounds
    while rounds<3:
        print("\nChoose one of:", ", ".join(choices))

        # THIRD WHILE LOOP: Validating user input
        while True:
            user_choice = input("👉 Your choice: ").lower()
            if user_choice in choices:
                break
            else:
                print("❌ Invalid choice! Try again.")

        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("😐 It's a tie!")
        elif computer_choice in rules[user_choice]:
            print("✅ You win!")
            player_score += 1
        else:
            print("❌ Computer wins!")
            computer_score += 1

        rounds += 1

    # Ask if the user wants to continue this match
    continue_round = input("\n🔁 Do you want to play another round? (yes/no): ").lower()
    if continue_round != "yes":
        break

# End of game stats
print("\n🎮 Game Over!")
print(f"📊 Total rounds played: {rounds}")
print(f"👤 Your score: {player_score}")
print(f"🤖 Computer score: {computer_score}")

if player_score > computer_score:
  print("🏆 Congratulations, you won the game!")
elif player_score < computer_score:
  print("💀 You lost the game. Better luck next time!")
else:
  print("😐 It's an overall tie!")

# Ask if the user wants to restart the whole game
play_again = input("\n🔄 Do you want to play a new game from scratch? (yes/no): ").lower()
if play_again != "yes":
  print("👋 Thanks for playing! Goodbye.")

