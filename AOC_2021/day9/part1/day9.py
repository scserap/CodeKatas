import itertools
from datetime import datetime
from functools import reduce

from AOC_2021.day1.day1 import read_file
import numpy as np


def get_sum_of_risk_levels(levels):
    lowest_numbers = []
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
                lowest_numbers.append(check_number+1)

    return sum(lowest_numbers)


def main():
    print(datetime.now())
    dataset = read_file('real_dataset.txt')
    levels = np.zeros([len(dataset),len(dataset[0])-1])
    # print(levels)
    for i in range(len(dataset)):
        # print(np.array(list(dataset[i].replace('\n',''))))
        levels[i] = np.array(list(dataset[i].replace('\n','')))
        # levels[i]=np.array(list(dataset[i].replace('\n','')))
    sum_of_risk_levels = get_sum_of_risk_levels(levels)
    print('sum_of_risk_levels is {}'.format(sum_of_risk_levels))
    print(datetime.now())

if __name__ == "__main__":
    main()