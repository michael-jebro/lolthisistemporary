import random

ELEMENTS = ["fire", "scissors", "snake", "human", "tree", "wolf", "sponge", "paper", "air", "water", "dragon", "devil", "lightning", "gun", "rock"]

def get_user_choice():
    user_choice = input("Choose element: " + ', '.join(ELEMENTS) + "? ").lower()
    while user_choice not in ELEMENTS:
        user_choice = input("Wrong choice! Choose element from: " + ', '.join(ELEMENTS) + "? ").lower()
    return user_choice

def determine_winner(user, computer):
    if user == computer:
        return "Draw!"
    
    user_index = ELEMENTS.index(user)
    computer_index = ELEMENTS.index(computer)
    winning_range = range(user_index + 1, user_index + 8)
    
    if computer_index in winning_range:
        return "You won!"
    return "You lose!"

def main():
    print("Welcome to modified version of scissors, rock, paper!")
    user_choice = get_user_choice()
    computer_choice = random.choice(ELEMENTS)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
