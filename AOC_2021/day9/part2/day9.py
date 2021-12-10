import itertools
from datetime import datetime
from functools import reduce

from AOC_2021.day1.day1 import read_file
import numpy as np

def get_risk_levels(levels):
    risk_levels = []
    lowest_number_positions = []
    for row_number in range(len(levels)):
        for column_number in range(len(levels[0])):
            check_number = levels[row_number][column_number]
            # print('check_number = {},column_number={}'.format(check_number,column_number))
            lower_than_left = False
            lower_than_right = False
            lower_than_up = False
            lower_than_bottom = False
            if column_number<len(levels[0])-1 :
                if check_number<levels[row_number][column_number+1]:
                    lower_than_right = True
            else:
                lower_than_right = True

            if row_number < len(levels)-1:
                if check_number < levels[row_number+1][column_number]:
                    lower_than_bottom = True
            else:
                lower_than_bottom = True

            if column_number > 0:
                if check_number < levels[row_number][column_number - 1]:
                    lower_than_left = True
            else:
                lower_than_left = True

            if row_number > 0:
                if check_number < levels[row_number - 1][column_number]:
                    lower_than_up = True
            else:
                lower_than_up = True
            if lower_than_up and lower_than_left and lower_than_bottom and lower_than_right:
                lowest_number_positions.append([row_number,column_number])
                risk_levels.append(check_number+1)

    return risk_levels, lowest_number_positions


def find_next_basin(basins, candidates,levels):
    # print(levels)
    # print(basins)
    positions = []
    for candidate in candidates:
        # print('candidate={}'.format(candidate))
        row = candidate[0]
        column = candidate[1]
        # print('row={},column={}'.format(row, column))
        if column>0: # left
            new_position = [row,column-1]
            # print('new_position={}'.format(new_position))
            if new_position not in basins and levels[row,column-1]<9:
                positions.append(new_position)
        if row<len(levels)-1: # down
            new_position = [row +1, column]
            # print('new_position={}'.format(new_position))
            if new_position not in basins and levels[row +1, column] < 9:
                positions.append(new_position)
        if column<len(levels[row])-1: # right
            new_position = [row,column+1]
            # print('new_position={}'.format(new_position))
            if new_position not in basins and levels[row,column+1]<9:
                positions.append(new_position)
        if row>0: # up
            new_position = [row -1, column]
            # print('new_position={}'.format(new_position))
            if new_position not in basins and levels[row -1, column] < 9:
                positions.append(new_position)
    if len(positions)>0:
        for position in positions:
            candidates.append(position)
    else:
        candidates.remove(candidate)
    return positions,candidates


def add_basins(found_basins, basins):
    for basin in found_basins:
        if basin not in basins:
            basins.append(basin)
    return basins


def get_basin_count(position,levels):
    candidates = []
    basins = []
    basin = position
    while len(candidates)>0 or len(basin)>0:
        if basin not in basins:
            basins.append(basin)
            candidates.append(basin)
        # print('basin={},candidates={}'.format(basin,candidates))
        found_basins, candidates = find_next_basin(basins, candidates, levels)
        if len(found_basins)==0 and len(candidates)==0:
            break
        basins = add_basins(found_basins,basins)
    print(basins)
    return len(basins)


def get_basins(lowest_number_positions,levels):
    basin_counts = np.zeros(len(lowest_number_positions))
    for i in range(len(lowest_number_positions)):
        basin_counts[i] = get_basin_count(lowest_number_positions[i],levels)
    basin_counts = sorted(basin_counts, reverse=True)
    multiply_of_basin_groups = 1
    for i in range(0,3):
        multiply_of_basin_groups *= basin_counts[i]
    return multiply_of_basin_groups


def main():
    print(datetime.now())
    dataset = read_file('real_dataset.txt')
    levels = np.zeros([len(dataset),len(dataset[0])-1])
    # print(levels)
    for i in range(len(dataset)):
        levels[i] = np.array(list(dataset[i].replace('\n','')))
    risk_levels, lowest_number_positions = get_risk_levels(levels)
    basin_counts = get_basins(lowest_number_positions,levels)
    print('sum_of_risk_levels is {}'.format(sum(risk_levels)))
    print('multiply_of_basin_groups is {}'.format(basin_counts))
    print(datetime.now())

if __name__ == "__main__":
    main()
