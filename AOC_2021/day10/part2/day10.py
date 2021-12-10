import itertools
from datetime import datetime
from functools import reduce

from AOC_2021.day1.day1 import read_file
import numpy as np

OPEN = ['(', '[', '{', '<']
CLOSE = [')', ']', '}', '>']
SCORE = [3,57,1197,25137]
SCORE2 = [1,2,3,4]
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



def get_second_score(char):
    for i in range(len(OPEN)):
        if OPEN[i]==char:
            return SCORE2[i]

def get_error_score(navigations):
    errors = []
    incomplete = []
    for navigation in navigations:
        new_navigation = ''
        error = False
        for char in navigation:
            if get_char_type(char):
                new_navigation += char
            else:
                if char == get_close_char(new_navigation[len(new_navigation)-1]):
                    new_navigation = new_navigation[0:len(new_navigation)-1]
                else:
                    error = True
                    navigations = np.delete(navigations, np.argwhere(navigations == navigation))
                    errors.append(char)
                    break
        if not error: incomplete.append(new_navigation)
    score = 0
    for error in errors:
        score += get_score(error)
    print(incomplete)
    scores = []
    for row in incomplete:
        row = row[::-1]
        # print(row)
        score2 = 0
        for char in row:
            score2 = (score2*5) + get_second_score(char)
        # print(score2)
        scores.append(score2)
    scores = sorted(scores)
    print(scores)
    print(int(len(scores) / 2))
    result_score = scores[int(len(scores) / 2)]
    return score,result_score


def main():
    print(datetime.now())
    dataset = read_file('real_dataset.txt')
    navigations = np.array(dataset)
    navigations = np.char.replace(navigations,'\n','')
    score,score2 = get_error_score(navigations)
    print('total syntax error score is {}, second score is {}'.format(score,score2))
    # wrong 3092339547
    # print(datetime.now())

if __name__ == "__main__":
    main()