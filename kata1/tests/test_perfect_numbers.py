import pytest
from kata1.perfect_numbers import get_perfect_number, get_perfect_number_list, is_perfect_number, main, \
    get_sum_of_digits


@pytest.mark.parametrize('number, expected', [
    (1, 1),
    (19, 10),
    (107, 8),
    (158, 14)
])
def test_get_sum_of_digits(number, expected):
    result = get_sum_of_digits(number)
    assert result == expected


@pytest.mark.parametrize('number, expected', [
    (1, False),
    (19, True),
    (10, False),
    (108, False),
    (118, True),
    (100036, True)
])
def test_is_perfect_number(number, expected):
    result = is_perfect_number(number)
    assert result == expected


@pytest.mark.parametrize('sequence, expected', [
    (1, 19),
    (2, 28),
    (10, 109),
    (100, 1423),
])
def test_get_perfect_number(sequence, expected):
    result = get_perfect_number(sequence)
    assert result == expected


@pytest.mark.parametrize('sequence', [
    1, 10, 100, 1000
])
def test_get_perfect_number_list(sequence):
    result_set = get_perfect_number_list(sequence)
    for result in result_set:
        assert sum(int(digit) for digit in str(result)) == 10
        # assert get_sum_of_digits_till_one_digit(result) == 10


def test_main():
    with pytest.raises(ValueError):
        main()


