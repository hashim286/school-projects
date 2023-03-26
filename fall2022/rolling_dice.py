import random


def roll_one_die(): # rolls a die as long as user wants
    while True:
        num_rolled = random.randint(1, 6)
        print(f"You rolled {num_rolled}")
        loop_again = input("Want to roll again? ").upper()
        if loop_again != 'N':
            break
    

def roll_600_times(): # tracking times each number is rolled with 600 simulated rolls
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    for i in range(600):
        num_rolled = random.randint(1, 6)
        if num_rolled == 1:
            ones += 1
        elif num_rolled == 2:
            twos += 1
        elif num_rolled == 3:
            threes += 1
        elif num_rolled == 4:
            fours += 1
        elif num_rolled == 5:
            fives += 1
        elif num_rolled == 6:
            sixes += 1
    
    print(f"1 was rolled {ones} times, percentage is {(ones/600)*100:.1f}%")
    print(f"2 was rolled {twos} times, percentage is {(twos/600)*100:.1f}%")
    print(f"3 was rolled {threes} times, percentage is {(threes/600)*100:.1f}%")
    print(f"4 was rolled {fours} times, percentage is {(fours/600)*100:.1f}%")
    print(f"5 was rolled {fives} times, percentage is {(fives/600)*100:.1f}%")
    print(f"6 was rolled {sixes} times, percentage is {(sixes/600)*100:.1f}%")


def roll_two_die(): # rolls two die, keeps track of number of rolls, quits out when 2 doubles are rolled
    rolls = 1
    doubles_rolled = 0
    while True:
        roll_one = random.randint(1, 6)
        roll_two = random.randint(1, 6)

        print(f"Roll #{rolls} - You rolled {roll_one} and {roll_two}")
        rolls += 1

        if roll_one == roll_two:
            print("You rolled a double!")
            doubles_rolled += 1

        if doubles_rolled == 2:
            break

    print("Congrats, you rolled 2 doubles, thanks for playing!")


def main():
    roll_one_die()
    roll_600_times()
    roll_two_die()


main()
