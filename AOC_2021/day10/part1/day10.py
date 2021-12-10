import itertools
from datetime import datetime
from functools import reduce

from AOC_2021.day1.day1 import read_file
import numpy as np

OPEN = ['(', '[', '{', '<']
CLOSE = [')', ']', '}', '>']
SCORE = [3,57,1197,25137]
def get_char_type(char):
    for i in range(len(OPEN)):
        if OPEN[i]==char:
            return True
        if CLOSE[i]==char:
            return False


def get_close_char(char):
    for i in range(len(OPEN)):
        if OPEN[i]==char:
            return CLOSE[i]


def get_score(char):
    for i in range(len(CLOSE)):
        if CLOSE[i]==char:
            return SCORE[i]


def get_error_score(navigations):
    errors = []
    for navigation in navigations:
        new_navigation = ''
        for char in navigation:
            if get_char_type(char):
                new_navigation += char
            else:
                if char == get_close_char(new_navigation[len(new_navigation)-1]):
                    new_navigation = new_navigation[0:len(new_navigation)-1]
                else:
                    errors.append(char)
                    break
    score = 0
    for error in errors:
        score += get_score(error)
    return score


def main():
    print(datetime.now())
    dataset = read_file('real_dataset.txt')
    navigations = np.array(dataset)
    navigations = np.char.replace(navigations,'\n','')
    score = get_error_score(navigations)
    print('total syntax error score is {}'.format(score))
    # print(datetime.now())

if __name__ == "__main__":
    main()