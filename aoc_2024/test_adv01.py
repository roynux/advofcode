from io import StringIO
import pytest

from aoc_2024.adv01 import compute_distances, compute_similarities, load_csv


@pytest.fixture
def get_list_fixture():
    return """3   4
4   3
2   5
1   3
3   9
3   3
"""


def test_load_csv(get_list_fixture):
    a, b = load_csv(StringIO(get_list_fixture))
    assert a == [3, 4, 2, 1, 3, 3]
    assert b == [4, 3, 5, 3, 9, 3]


def test_adv01(get_list_fixture):
    a, b = load_csv(StringIO(get_list_fixture))
    assert a == [3, 4, 2, 1, 3, 3]
    assert b == [4, 3, 5, 3, 9, 3]

    distances = compute_distances(a, b)
    assert distances == [2, 1, 0, 1, 2, 5]

    assert sum(distances) == 11

    similarities = compute_similarities(a, b)
    assert similarities == [9, 4, 0, 0, 9, 9]
