import argparse


def get_sum_of_digits(number):
    return sum(map(int, str(number)))


def is_perfect_number(perfect_number_candidate):
    return True if get_sum_of_digits(perfect_number_candidate) == 10 else False


def get_perfect_number_list(sequence):
    perfect_numbers, perfect_number_candidate = [], 1
    while len(perfect_numbers) < sequence:
        perfect_number_candidate += 9
        if is_perfect_number(perfect_number_candidate): perfect_numbers.append(perfect_number_candidate)
    return perfect_numbers


def get_perfect_number(sequence):
    perfect_numbers = get_perfect_number_list(sequence)
    perfect_number = perfect_numbers[sequence - 1]
    print('Considering a perfect number as an integer that the sum of its digits equal 10, The Perfect Number {sequence} is {perfect_number}'.format(sequence=sequence, perfect_number=perfect_number))
    return perfect_number


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sequence', type=int, help='a positive integer n, to return n-th perfect number')
    args = parser.parse_args()
    if args.sequence: get_perfect_number(args.sequence)
    else: raise ValueError("Sequence arg needs to be provided")


if __name__ == "__main__":
    main()

