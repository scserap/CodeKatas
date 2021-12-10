from datetime import datetime

from AOC_2021.day1.day1 import read_file
import numpy as np


def pass_days(fishes,days):
    for day in range(1, days + 1):
        # print(day)
        baby_fish_count = np.count_nonzero(fishes==0)
        baby_fishes = np.full(baby_fish_count, 8)
        mummy_fishes = np.full(baby_fish_count, 6)
        fishes = fishes[fishes > 0] - 1
        fishes = np.concatenate([fishes,baby_fishes,mummy_fishes])
    lanternfish_count = len(fishes)

    return lanternfish_count


def main():
    print(datetime.now())
    current_fishes = read_file('test_dataset.txt')
    day_count = 80
    fishes = np.array(current_fishes[0].split(','), int)
    lanternfish_count = pass_days(fishes = fishes, days=day_count)
    print('Total Lantern Fish Count after {} days is {}'.format(day_count,lanternfish_count))
    print(datetime.now())

if __name__ == "__main__":
    main()