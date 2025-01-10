import pytest

from aoc_2024.adv09 import (
    map_disk,
    blocks_defrag,
    part1,
    find_sequence,
    find_space,
    files_defrag,
    part2,
)


@pytest.fixture
def example_1():
    return "2333133121414131402"


@pytest.fixture
def example_1_blocks():
    # return "00...111...2...333.44.5555.6666.777.888899"
    return [
        0,
        0,
        None,
        None,
        None,
        1,
        1,
        1,
        None,
        None,
        None,
        2,
        None,
        None,
        None,
        3,
        3,
        3,
        None,
        4,
        4,
        None,
        5,
        5,
        5,
        5,
        None,
        6,
        6,
        6,
        6,
        None,
        7,
        7,
        7,
        None,
        8,
        8,
        8,
        8,
        9,
        9,
    ]


@pytest.fixture
def example_1_defrag():
    #  "0099811188827773336446555566.............."
    return [
        0,
        0,
        9,
        9,
        8,
        1,
        1,
        1,
        8,
        8,
        8,
        2,
        7,
        7,
        7,
        3,
        3,
        3,
        6,
        4,
        4,
        6,
        5,
        5,
        5,
        5,
        6,
        6,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]


@pytest.fixture
def example_2():
    return "12345"


@pytest.fixture
def example_2_blocks():
    # "0..111....22222"
    return [0, None, None, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]


@pytest.fixture
def example_2_defrag():
    # "022111222......"
    return [0, 2, 2, 1, 1, 1, 2, 2, 2, None, None, None, None, None, None]


def test_map_disk(
    example_1,
    example_1_blocks,
    example_2,
    example_2_blocks,
):
    disk, last_file_id = map_disk(example_2)
    assert disk == example_2_blocks
    assert last_file_id == 2

    disk, last_file_id = map_disk(example_1)
    assert disk == example_1_blocks
    assert last_file_id == 9


def test_blocks_defrag(
    example_1_blocks, example_1_defrag, example_2_blocks, example_2_defrag
):
    disk = example_2_blocks.copy()
    blocks_defrag(disk)
    assert disk == example_2_defrag

    disk = example_1_blocks.copy()
    blocks_defrag(disk)
    assert disk == example_1_defrag


def test_part1(example_1, example_2):
    assert part1(example_1) == 1928
    assert part1(example_2) == 60


@pytest.fixture
def example_3():
    # return "000...1....2222.3333.444"
    # "0004441....2222.3333....""
    # "000444133332222.........""
    return "3314414133"


@pytest.fixture
def example_3_blocks():
    return [
        0,
        0,
        0,
        None,
        None,
        None,
        1,
        None,
        None,
        None,
        None,
        2,
        2,
        2,
        2,
        None,
        3,
        3,
        3,
        3,
        None,
        4,
        4,
        4,
        None,
        None,
        None,
    ]


def test_find_sequence(example_3_blocks):
    assert find_sequence(example_3_blocks, 0) == (0, 3)
    assert find_sequence(example_3_blocks, 0, 1) == (1, 2)
    assert find_sequence(example_3_blocks, 0, 10) == (-1, 0)
    assert find_sequence(example_3_blocks, 2) == (11, 4)
    assert find_sequence(example_3_blocks, None) == (3, 3)
    assert find_sequence(example_3_blocks, None, 6) == (7, 4)


def test_find_space(example_3_blocks):
    assert find_space(example_3_blocks, 0) == (-1)
    assert find_space(example_3_blocks, 2) == (3)
    assert find_space(example_3_blocks, 3) == (3)
    assert find_space(example_3_blocks, 4) == (7)
    assert find_space(example_3_blocks, 5) == (-1)


@pytest.fixture
def example_3_defrag():
    return [
        0,
        0,
        0,
        4,
        4,
        4,
        1,
        3,
        3,
        3,
        3,
        2,
        2,
        2,
        2,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]


def test_files_defrag(example_3_blocks, example_3_defrag):
    disk = example_3_blocks.copy()
    last_file_id = 4
    files_defrag(disk, last_file_id)
    assert disk == example_3_defrag


def test_part2(example_1, example_2, example_3):
    assert part2(example_1) == 2858
    assert part2(example_2) == 132
    assert part2(example_3) == 256
