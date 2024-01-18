import random

def play_game():
    print("\nRock, Paper, Scissors Game\n")
    print("Choose your option:")
    print("r - Rock")
    print("p - Paper")
    print("s - Scissors")

    user_choice = input("Your choice: ")

    if user_choice not in ["r", "p", "s"]:
        print("Invalid choice! Please choose 'r', 'p', or 's'.")
        return

    options = ["r", "p", "s"]
    computer_choice = random.choice(options)

    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "s" and computer_choice == "p"):
        print("You win the game!")
    else:
        print("You lose the game!")

if __name__ == "__main__":
    while True:
        input("Press any key to start or 'q' to exit: ")
        play_game()

        play_again = input("Press any key to play again or 'q' to exit: ")
        if play_again.lower() == "q":
            print("Thanks for playing. Goodbye!")
            break
