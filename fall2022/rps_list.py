import random

choices = ["Rock", "Paper", "Scissors"]



def user_choose_rps() -> int: # validate user input, make sure number is between 1 and 3
    while True:
        try:
            choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for scissors: "))
        except ValueError:
            print("Please enter an integer 1-3")
        else:
            if choice == 1 or choice == 2 or choice == 3:
                return choice
            print("The number must be between 1 and 3")



def determine_winner(user_choice: int, computer_choice: int) -> str: # calculates the winner with 2 integers 1-3 representing computer and user_choice
    if user_choice == computer_choice:
        return "It's a tie"
    elif user_choice - computer_choice == 1 or computer_choice - user_choice == 2:
        return "You win"
    else:
        return "You lose"


def main():
    game_history = list()
    while True:
        user_choice = user_choose_rps() - 1
        computer_choice = random.randint(0, 2)
        print(f"You chose {choices[user_choice]}")
        print(f"The computer chose {choices[computer_choice]}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        game_history.append([user_choice, computer_choice, result]) # adds the choices and result to a game history list which is printed at the end when user quits

        loop_again = input("Do you want to play again? Type N to quit or anything to continue: ").upper()
        if loop_again == "N":
            print("\nHere is your game history, thanks for playing!\n")

            game_number = 1
            for game in game_history:
                print(f"Game {game_number}: You chose {choices[game[0]]}, the computer chose {choices[game[1]]}, "
                    f"and the result was {game[2]}")
                game_number += 1
                
            break


main()