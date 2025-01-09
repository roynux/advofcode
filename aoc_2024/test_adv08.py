import pytest

from aoc_2024.adv08 import (
    decode_map,
    generate_combinations,
    compute_antinodes,
    part_1,
    part_2,
)


@pytest.fixture
def example1():
    return """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()


@pytest.fixture
def example2():
    return """..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
..........""".splitlines()


@pytest.fixture
def example3():
    return """..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......A...
..........
..........""".splitlines()


def test_decode_map(example1, example2, example3):
    # example1
    height, width, antennas = decode_map(example1)
    assert height == 12
    assert width == 12
    assert antennas["0"] == {(1, 8), (2, 5), (3, 7), (4, 4)}
    assert antennas["A"] == {(5, 6), (8, 8), (9, 9)}

    # example2
    height, width, antennas = decode_map(example2)
    assert height == 10
    assert width == 10
    assert antennas["a"] == {(3, 4), (5, 5)}
    # assert antennas["#"] == {(7, 6), (1, 3)}

    # example3
    height, width, antennas = decode_map(example3)
    assert height == 10
    assert width == 10
    assert antennas["a"] == {(3, 4), (4, 8), (5, 5)}
    # assert antennas["#"] == {(1, 3), (2, 0), (6, 2), (7, 6)}


def test_generate_combinations():
    input_set = {(1, 8), (2, 5), (3, 7), (4, 4)}
    expected_output = [
        ((4, 4), (3, 7)),
        ((4, 4), (1, 8)),
        ((4, 4), (2, 5)),
        ((3, 7), (1, 8)),
        ((3, 7), (2, 5)),
        ((1, 8), (2, 5)),
    ]
    assert generate_combinations(input_set) == expected_output


def test_compute_antinodes(example3):
    height = 10
    width = 10
    antennas_locations = {(3, 4), (5, 5)}
    antinodes = compute_antinodes(height, width, antennas_locations)
    assert antinodes == {(7, 6), (1, 3)}

    antennas_locations = {(3, 4), (4, 8), (5, 5)}
    antinodes = compute_antinodes(height, width, antennas_locations)
    assert antinodes == {(7, 6), (2, 0), (1, 3), (6, 2)}

    height, width, antennas = decode_map(example3)
    assert height == 10
    assert width == 10
    assert antennas["a"] == {(3, 4), (4, 8), (5, 5)}
    assert antennas["A"] == {(7, 6)}

    antinodes = set()
    for antenna, locations in antennas.items():
        # print(f"Antenna {antenna}: {locations}")
        new_antinodes = compute_antinodes(height, width, locations)
        antinodes.update(new_antinodes)
        # print(f"Antinodes: {new_antinodes}")
    # assert antennas["#"] == {(1, 3), (2, 0), (6, 2), (7, 6)}
    print(f"Total Antinodes: {antinodes}")
    assert antinodes == {(2, 0), (6, 2), (7, 6), (1, 3)}


def test_part_1(example1):
    all_antennas, antinodes, all_antinodes = part_1(example1)
    assert antinodes == {
        (0, 11),
        (0, 6),
        (1, 3),
        (10, 10),
        (11, 10),
        (2, 10),
        (2, 4),
        (3, 2),
        (4, 9),
        (5, 1),
        (5, 6),
        (6, 3),
        (7, 0),
        (7, 7),
    }
    print(f"All Antennas: {all_antennas}")
    print(f"Antennas ovrelapping antinodes: {all_antennas & antinodes}")
    print(f"Antinodes not overlapping Antennas: {antinodes - all_antennas}")
    assert len(antinodes) == 14


@pytest.fixture
def example4():
    return """..........
#..a..a..#
..........
...a......
..........
#..#......
..........
...#......
..........
...#......""".splitlines()


@pytest.fixture
def example4_expected_antinodes_full_line():
    return {(1, 0), (1, 9), (5, 0), (5, 3), (7, 3), (9, 3)}


@pytest.fixture
def example6():
    return """T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........""".splitlines()


def test_compute_antinodes_full_line(
    example4, example4_expected_antinodes_full_line, example6
):
    height, width, antennas = decode_map(example4)
    antinodes = compute_antinodes(height, width, antennas["a"], full_line=True)
    print(f"Antinodes: {antinodes}")
    assert antinodes == example4_expected_antinodes_full_line

    height, width, antennas = decode_map(example6)
    antinodes = compute_antinodes(height, width, antennas["T"], full_line=True)
    print(f"Antinodes: {antinodes}")
    assert len(antinodes) == 6


def test_part_2(example1, example6):
    # all_antennas, antinodes, all_antinodes = part_2(example6)
    # assert len(antinodes) == 6
    all_antennas, antinodes, all_antinodes = part_2(example1)

    assert len(antinodes) == 34
