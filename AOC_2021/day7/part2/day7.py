from datetime import datetime

from AOC_2021.day1.day1 import read_file
import numpy as np


def sum_of_numbers(position, ideal_position):
    total = 0
    for i in range(1,abs(ideal_position-position)+1):
        total += i
    return total


def get_ideal_position(positions):
    return round(np.mean(positions,dtype=np.int64))


def calculate_minimum_fuel(positions):
    max_value = np.max(positions)
    necessary_fuel = np.zeros(max_value)
    print('max_value={}'.format(max_value))
    for ideal_position in range(1,max_value+1):
        print('Aligning Position={}'.format(ideal_position))
        for i in range(0,len(positions)):
            necessary_fuel[ideal_position-1] += sum_of_numbers(positions[i], ideal_position)
    result = np.amin(necessary_fuel)
    return(result)

def main():
    print(datetime.now())
    position_dataset = read_file('real_dataset.txt')
    positions = np.array(position_dataset[0].split(','), dtype=np.int64)
    minimum_fuel = calculate_minimum_fuel(positions = positions)
    print('Minimum_fuel is {}'.format(minimum_fuel))
    print(datetime.now())
#   mean 476 96361630 wrong
#   mean with round 96361606 correct

if __name__ == "__main__":
    main()