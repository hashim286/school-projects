import random

while True:
    # take user input for their choice between rock paper scissors which corresponds to 1, 2, 3 respectively
    user_choice = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))
    # computer generates random num between 1, 3 with random.randint
    computer_choice = random.randint(1, 3)


    # print user choice
    if user_choice == 1:
        print("You chose rock")
    elif user_choice == 2:
        print("You chose paper")
    else:
        print("You chose scissors")

    # print computer choice
    if computer_choice == 1:
        print("Computer chose rock")
    elif computer_choice == 2:
        print("Computer chose paper")
    elif computer_choice == 3:
        print("Computer chose scissors")


    if user_choice == computer_choice:
        print("It's a tie")
    elif user_choice - computer_choice == 1 or computer_choice - user_choice == 2: # when difference is +1, higher number always wins, if it is +2, lower number wins
        print("You win!")
    else: # all lose conditions are caught here
        print("You lose!")

    # Ask the user if they would like to continue
    ask_loop_again = input("Type N to quit or type anything to continue: ").upper()

    # restart program if yes, if not, quit out with goodbye msg
    print("\n")

    if ask_loop_again == "N":
        break

print("Thanks for playing!")