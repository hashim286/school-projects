import random


def user_choose_rps() -> int: # input validation from user so function won't break, also verifies a number 1-3 was entered
    while True:
        try:
            choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for scissors: "))
        except ValueError:
            print("Please enter an integer 1-3")
        else:
            if choice == 1 or choice == 2 or choice == 3:
                return choice


def determine_choices(choice: int) -> str: # determine user and computer choice for an inputted number
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"


def determine_winner(user_choice: int, computer_choice: int): # takes 2 ints for user and computer choice and prints winner
    if user_choice == computer_choice:
        print("It's a tie")
    elif user_choice - computer_choice == 1 or computer_choice - user_choice == 2:
        print("You win")
    else:
        print("You lose")


def main():
    user_choice = user_choose_rps()
    computer_choice = random.randint(1, 3)

    user_print = determine_choices(user_choice)
    computer_print = determine_choices(computer_choice)

    print(f"You chose {user_print}")
    print(f"The computer chose {computer_print}")

    determine_winner(user_choice, computer_choice)

    loop_again = input("Do you want to play again? Type N to quit or press anything to continue: ").upper()
    if loop_again != "N":
        main()
    else:
        print("Goodbye!")


main()
