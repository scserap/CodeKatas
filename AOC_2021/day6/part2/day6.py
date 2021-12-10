from datetime import datetime

from AOC_2021.day1.day1 import read_file
import numpy as np


def pass_days(fishes,days):
    fish_count = np.zeros(9)
    for fish in fishes:
        fish_count[fish] += 1
    for day in range(1, days + 1):
        new_fish_count = np.zeros(9)
        for i in range(8,0,-1):
            new_fish_count[i-1] = fish_count[i]
        new_fish_count[8] += fish_count[0]
        new_fish_count[6] += fish_count[0]
        fish_count = new_fish_count
    lanternfish_count = sum(fish_count)
    return lanternfish_count


def main():
    print(datetime.now())
    current_fishes = read_file('real_dataset.txt')
    day_count = 256
    fishes = np.array(current_fishes[0].split(','), int)
    lanternfish_count = pass_days(fishes = fishes, days=day_count)
    print('Total Lantern Fish Count after {} days is {}'.format(day_count,lanternfish_count))
    print(datetime.now())
#     1682576647495

if __name__ == "__main__":
    main()
