from datetime import datetime

from AOC_2021.day1.day1 import read_file
import numpy as np

ALL_DIGITS = np.array(['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'])
CHARLIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


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



def does_contain(code, digit_number):
    if ''.join(sorted(list(code))) in ''.join(sorted(ALL_DIGITS[digit_number])):
        return True
    else:
        return False



def get_sum_of_all_four_digits(four_digits,row_digits):
    multiplier = [1000,100,10,1]
    sum_of_all_four_digits = 0
    for four_digit_index in range(0,4):
        print('four_digits[digit_index]={}'.format(four_digits[four_digit_index]))
        for digit_index in range(len(row_digits)):
            if does_contain(row_digits[digit_index],four_digits[four_digit_index]) and len(row_digits[digit_index]) == len(four_digits[four_digit_index]):
                print('digit_index={},row_digits[digit_index]={}, common={},len={}'.format(digit_index,row_digits[digit_index],get_common_char_count(four_digits[four_digit_index],row_digits[digit_index]),len(four_digits[four_digit_index])))
                print(digit_index * multiplier[four_digit_index])
                sum_of_all_four_digits += (digit_index * multiplier[four_digit_index])
    print('four_digits={}, sum_of_all_four_digits={}'.format(four_digits,sum_of_all_four_digits))
    return sum_of_all_four_digits
    # print(number)



def does_contain(code, other_code):
    for char in other_code:
        if not char in code:
               return False
    return True


def get_common_char_count(code,other_code):
    common_char_count = 0
    for char in code:
        if char in other_code:
            common_char_count += 1
    return common_char_count


def get_decoded_sum(notes, four_digits):
    sum_of_all_four_digits = 0
    for row_number in range(len(notes)):
        row = notes[row_number]
        row_digits = np.empty_like(ALL_DIGITS)
        for digit_code in row:
            if len(digit_code) == 2:
                row_digits[1] = digit_code
            elif len(digit_code) == 4:
                row_digits[4] = digit_code
            elif len(digit_code) == 3:
                row_digits[7] = digit_code
            elif len(digit_code) == 7:
                row_digits[8] = digit_code
        for digit_code in row:
            if len(digit_code) == 5 and does_contain(digit_code,row_digits[7]):
                row_digits[3] = digit_code
        for digit_code in row:
            if len(digit_code) == 6 and not does_contain(digit_code,row_digits[1]):
                row_digits[6] = digit_code
        for digit_code in row:
            if len(digit_code) == 5 and get_common_char_count(digit_code,row_digits[6])==5:
                row_digits[5] = digit_code
        for digit_code in row:
            if len(digit_code) == 5 and not does_contain(digit_code, row_digits[1]) and get_common_char_count(digit_code,row_digits[4])==2:
                row_digits[2] = digit_code
        for digit_code in row:
            if len(digit_code) == 6 and does_contain(digit_code,row_digits[1]) and does_contain(digit_code,row_digits[7]) and not does_contain(digit_code,row_digits[4]):
                row_digits[0] = digit_code
        for digit_code in row:
            if len(digit_code) == 6 and does_contain(digit_code,row_digits[3]):
                row_digits[9] = digit_code


        print(row_digits)
        sum_of_all_four_digits += get_sum_of_all_four_digits(four_digits[row_number],row_digits)
    return sum_of_all_four_digits

def main():
    print(datetime.now())
    dataset = read_file('real_dataset.txt')
    notes, four_digits = clean_dataset(dataset)
    sum_of_all_four_digits = get_decoded_sum(notes, four_digits)
    print('sum_of_all_four_digits is {}'.format(sum_of_all_four_digits))
    print(datetime.now())

if __name__ == "__main__":
    main()