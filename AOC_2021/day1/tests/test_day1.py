from AOC_2021.day1.day1 import get_how_many_times_increased, read_file


def test_get_how_many_times_increased():
    measurements = read_file('day1_testdata.txt')
    result = get_how_many_times_increased(measurements, 1)
    expected = 7
    result = get_how_many_times_increased(measurements,3)
    expected = 5
    assert result == expected