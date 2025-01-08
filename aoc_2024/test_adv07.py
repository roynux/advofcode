import pytest
import operator

from aoc_2024.adv07 import (
    compute_combinations,
    split_equation_lines,
    part_1,
    my_concat,
    part_2,
)


@pytest.fixture
def sample_data():
    return """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()


def test_split_line(sample_data):
    data = [equation_values for equation_values in split_equation_lines(sample_data)]
    assert data == [
        (190, [10, 19]),
        (3267, [81, 40, 27]),
        (83, [17, 5]),
        (156, [15, 6]),
        (7290, [6, 8, 6, 15]),
        (161011, [16, 10, 13]),
        (192, [17, 8, 14]),
        (21037, [9, 7, 18, 13]),
        (292, [11, 6, 16, 20]),
    ]


def test_compute_combinations():
    values = [81, 40, 27]
    operators = [operator.add, operator.mul]
    results = []
    compute_combinations(operators, results, values[0], values[1:])
    assert results == [148, 3267, 3267, 87480]


def test_part_1(sample_data):
    assert part_1(sample_data) == 3749


def test_my_concat():
    assert my_concat(1, 2) == 12
    assert my_concat(123, 456) == 123456


def test_part_2(sample_data):
    assert part_2(sample_data) == 11387
