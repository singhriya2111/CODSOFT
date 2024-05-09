import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nWelcome to Rock-Paper-Scissors!")
        print("Choose one: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose again.")
            continue
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Computer's choice:", computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print("Score - You:", user_score, "Computer:", computer_score)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
