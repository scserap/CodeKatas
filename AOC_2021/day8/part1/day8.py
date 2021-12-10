from datetime import datetime

from AOC_2021.day1.day1 import read_file
import numpy as np

ALL_DIGITS = np.array(['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'])

def clean_dataset(dataset):
    notes = []
    four_digits = []
    for row in dataset:
        row = row.replace('\n','')
        columns = row.split(' | ')
        notes.append(columns[0].split(' '))
        four_digits.append(columns[1].split(' '))
    notes = np.array(notes,dtype=str)
    four_digits = np.array(four_digits,dtype=str)
    # print('notes={}, four_digits={}'.format(notes, four_digits))
    return notes, four_digits


def get_unique_digits():

    unique_digit_lens = np.zeros(len(ALL_DIGITS))
    len_digits = np.zeros(len(ALL_DIGITS))
    for i in range(len(ALL_DIGITS)):
        unique_digit_lens[len(ALL_DIGITS[i])] += 1
        len_digits[i] = len(ALL_DIGITS[i])
    unique_digit_lens = np.where(unique_digit_lens == 1)[0]
    unique_digits = np.zeros(len(unique_digit_lens))
    for i in range(len(unique_digit_lens)):
        unique_digits[i] = np.where(len_digits == unique_digit_lens[i])[0]
    return unique_digits,unique_digit_lens


def get_count_of_easy_digits(notes, four_digits):
    unique_digits,len_digits = get_unique_digits()
    print(len_digits)
    number_of_appearance = 0
    for row in four_digits:
        for digit in row:
            print('digit={},len(digit)={},np.where={}'.format(digit,len(digit),np.where(len_digits==len(digit))[0]))
            if len(np.where(len_digits==len(digit))[0])>0:
                print(digit)
                number_of_appearance += 1
    print(number_of_appearance)
    return number_of_appearance


def main():
    print(datetime.now())
    dataset = read_file('real_dataset.txt')
    notes, four_digits = clean_dataset(dataset)
    count_of_easy_digits = get_count_of_easy_digits(notes, four_digits)
    print('count_of_easy_digits is {}'.format(count_of_easy_digits))
    print(datetime.now())
if __name__ == "__main__":
    main()