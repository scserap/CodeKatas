from AOC_2021.day3.first_part.day3 import get_binary_list, get_gamma_rate
from AOC_2021.day1.day1 import read_file


def test_move_submarine():
    report = read_file('day3_testdata.txt')
    binary_report = get_binary_list(report)
    gamma = str(get_gamma_rate(binary_report))
    assert gamma == '10110'
