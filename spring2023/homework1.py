# @file_name:   homework1.py
# @author:      Hashim Rauf
# #datetime:    3/10/2023 6:26 PM
# @description: Homework assignment 1

import numpy as np
import sys

ADJACENT_NUMBERS = 4


def main():
    """loads in an array from a file and prints the value of the largest sum of 4 adjacent numbers by default
     that are divisible by the divisor provided by the user at runtime. To change the adjacent numbers change the
     value of ADJACENT_NUMBERS at the top of the file"""
    generate_array_question = input("Generate a random array? ").lower()
    if generate_array_question == 'y':
        file_name = "text"
        generate_array(file_name)
    else:
        file_name = input("Enter the file name that contains the array, don't include the .txt extension: ")

    array = load_file(file_name)
    divisor = get_divisor()
    max_divisible_by_divisor = calc_max_sum(divisor, array)
    print(max_divisible_by_divisor)


def load_file(file_name):
    """returns a numpy array loaded from a file located in the same directory as the script or quits the program if
    the file is not found"""
    try:
        array = np.loadtxt(f"{file_name}.txt").astype(int)
    except FileNotFoundError:
        sys.exit(f"No text file called '{file_name}' in the directory, choose to generate one or provide one")
    else:
        return array


def get_divisor() -> int:
    """returns an integer from the user to be used as the divisor"""
    while True:
        try:
            divisor = int(input("Enter a divisor: "))
        except ValueError:
            print("Value must be an integer")
        else:
            return divisor


def calc_max_sum(divisor, array):
    """returns the maximum sum of 4 adjacent numbers (by default) in all directions
    that are divisible by the divisor provided by the user. To change how many adjacent numbers are considered change
    the value of ADJACENT_NUMBERS at the top of the file"""
    sums_divisible = list()
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if i <= array.shape[0] - ADJACENT_NUMBERS:
                sum_down = np.sum(array[i: i + ADJACENT_NUMBERS, j])
                if sum_down % divisor == 0:
                    sums_divisible.append(sum_down)


            if j <= array.shape[1] - ADJACENT_NUMBERS:
                sum_right = np.sum(array[i, j: j + ADJACENT_NUMBERS])
                if sum_right % divisor == 0:
                    sums_divisible.append(sum_right)


            diag_array_one = np.diagonal(array, offset=j)[i: i + ADJACENT_NUMBERS]
            sum_diag_array_one = np.sum(diag_array_one)

            if len(diag_array_one) == ADJACENT_NUMBERS and sum_diag_array_one % divisor == 0:
                sums_divisible.append(sum_diag_array_one)


            diag_array_two = np.diagonal(array, offset=-j)[i: i + ADJACENT_NUMBERS]
            sum_diag_array_two = np.sum(diag_array_two)

            if len(diag_array_two) == ADJACENT_NUMBERS and sum_diag_array_two % divisor == 0:
                sums_divisible.append(sum_diag_array_two)


            flipped_array = np.fliplr(array)
            flipped_diag_one = np.diagonal(flipped_array, offset=j)[i: i + ADJACENT_NUMBERS]
            sum_flipped_one = np.sum(flipped_diag_one)

            if len(flipped_diag_one) == ADJACENT_NUMBERS and sum_flipped_one % divisor == 0:
                sums_divisible.append(sum_flipped_one)


            flipped_diag_two = np.diagonal(flipped_array, offset=-j)[i: i + ADJACENT_NUMBERS]
            sum_flipped_two = np.sum(flipped_diag_two)

            if len(flipped_diag_two) == ADJACENT_NUMBERS and sum_flipped_two % divisor == 0:
                sums_divisible.append(sum_flipped_two)

    return max(sums_divisible) if len(sums_divisible) > 0 else 0


def generate_array(filename):
    array = np.array(np.random.randint(1, 100, (20, 20))).astype(int)
    np.savetxt(f'{filename}.txt', array, fmt='%i')


main()