from aoc_2024.adv04 import find_mas, find_xmas
import pytest


@pytest.fixture
def get_sample_data():
    return """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def test_find_xmas(get_sample_data):
    data = get_sample_data.split()
    assert find_xmas(data) == 18


def test_find_mas(get_sample_data):
    data = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........""".split()
    assert find_mas(data) == 9
