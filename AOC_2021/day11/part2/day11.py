from datetime import datetime

from AOC_2021.day1.day1 import read_file
import numpy as np


def flash_octopus(to_be_flashed_octopuses, octopuses,flashed_octopuses):
    for octopus in to_be_flashed_octopuses:
        row = octopus[0]
        column = octopus[1]
        if row + 1 < len(octopuses): octopuses[row + 1,column]  += 1  # down
        if row - 1 >= 0: octopuses[row - 1, column] += 1  # up
        if column - 1 >= 0: octopuses[row, column - 1] += 1  # left
        if column + 1 < len(octopuses[0]): octopuses[
            row, column + 1] += 1  # right
        if row + 1 < len(octopuses) and column - 1 >= 0: octopuses[
            row + 1, column - 1] += 1  # down left
        if row - 1 >= 0 and column - 1 >= 0: octopuses[
            row - 1, column - 1] += 1  # up left
        if row + 1 < len(octopuses) and column + 1 < len(octopuses[0]): octopuses[
            row + 1, column + 1] += 1  # down right
        if row - 1 >= 0 and column + 1 < len(octopuses[0]): octopuses[
            row - 1, column + 1] += 1  # up right
        flashed_octopuses.append(octopus)
    to_be_flashed_octopuses = get_next_flashing_octopus(octopuses,flashed_octopuses)
    return to_be_flashed_octopuses,octopuses, flashed_octopuses


def get_next_flashing_octopus(octopuses,flashed_octopuses):
    to_be_flashed_octopuses = []
    for row in range(len(octopuses)):
        for column in range(len(octopuses[0])):
            if octopuses[row,column]>9 and [row,column] not in flashed_octopuses:
                to_be_flashed_octopuses.append([row,column])
    return to_be_flashed_octopuses


def all_octopuses_flashed(flashed_octopuses,octopuses):
    for row in range(len(octopuses)):
        for column in range(len(octopuses[0])):
            if [row,column] not in flashed_octopuses:
                return False
    return True

def get_flash_count(octopuses):
    flash_counts = []
    print(octopuses)
    step = 0
    flashed_octopuses = []
    while not all_octopuses_flashed(flashed_octopuses,octopuses):
        flashed_octopuses = []
        step += 1
        octopuses += 1
        to_be_flashed_octopuses = get_next_flashing_octopus(octopuses, flashed_octopuses)
        while len(to_be_flashed_octopuses) > 0 :
            to_be_flashed_octopuses, octopuses,flashed_octopuses = flash_octopus(to_be_flashed_octopuses, octopuses,flashed_octopuses)
        print(octopuses)
        flash_counts.append(len(flashed_octopuses))
        octopuses[octopuses>9]=0
        print(flash_counts)
    return sum(flash_counts),step


def main():
    print(datetime.now())
    dataset = read_file('real_dataset.txt')
    octopuses = np.zeros([len(dataset), len(dataset[0]) - 1])
    for i in range(len(dataset)):
        octopuses[i] = np.array(list(dataset[i].replace('\n', '')))
    flash_count,step = get_flash_count(octopuses)

    print('total flash count is {}, step is {}'.format(flash_count,step))
    print(datetime.now())

if __name__ == "__main__":
    main()