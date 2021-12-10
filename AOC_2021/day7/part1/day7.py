from datetime import datetime

from AOC_2021.day1.day1 import read_file
import numpy as np


def calculate_minimum_fuel(positions):
    position = np.median(positions)
    necessary_fuel = np.sum(np.abs(positions-position))
    return(necessary_fuel)

def main():
    print(datetime.now())
    position_dataset = read_file('real_dataset.txt')
    positions = np.array(position_dataset[0].split(','), int)
    minimum_fuel = calculate_minimum_fuel(positions = positions)
    print('Minimum_fuel is {}'.format(minimum_fuel))
    print(datetime.now())

if __name__ == "__main__":
    main()