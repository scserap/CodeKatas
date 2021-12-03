from AOC_2021.day2.day2 import move_submarine
from AOC_2021.day1.day1 import read_file


def test_move_submarine():
    commands = read_file('day2_testdata.txt')
    result_horizontal_position, result_depth = move_submarine(commands)
    expected_horizontal_position = 15
    expected_depth = 60
    assert result_horizontal_position == expected_horizontal_position
    assert result_depth == expected_depth