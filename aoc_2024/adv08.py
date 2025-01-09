import string
from collections import defaultdict
from itertools import combinations


def decode_map(map):
    height, width = len(map), len(map[0])
    antennas = defaultdict(set)
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char in string.ascii_letters or char in string.digits or char == "#":
                antennas[char].add((y, x))
    return height, width, antennas


def generate_combinations(input_set):
    # Convert the set to a list for easier manipulation
    input_list = list(input_set)

    # Generate all combinations of 2 elements
    combinations_list = list(combinations(input_list, 2))

    return combinations_list


def compute_antinodes(h, w, locs, full_line=False):
    ants = set()
    if len(locs) > 0:
        for a1, a2 in generate_combinations(locs):
            y1, x1 = a1
            y2, x2 = a2
            if not full_line:
                anode1 = (y2 + y2 - y1, x2 + x2 - x1)
                if 0 <= anode1[0] < h and 0 <= anode1[1] < w:
                    ants.add(anode1)

                anode2 = (y1 + y1 - y2, x1 + x1 - x2)
                if 0 <= anode2[0] < h and 0 <= anode2[1] < w:
                    ants.add(anode2)
            else:
                dy = y2 - y1
                dx = x2 - x1
                ants.add(a2)
                new_y = y2 + dy
                new_x = x2 + dx
                while 0 <= new_y < h and 0 <= new_x < w:
                    ants.add((new_y, new_x))
                    new_y += dy
                    new_x += dx
                # move from a2 to a1 and continue
                ants.add(a1)
                dy = y1 - y2
                dx = x1 - x2
                new_y = y1 + dy
                new_x = x1 + dx
                while 0 <= new_y < h and 0 <= new_x < w:
                    ants.add((new_y, new_x))
                    new_y += dy
                    new_x += dx

    return ants


def part_1(mymap):
    height, width, antennas = decode_map(mymap)
    print(f"Height: {height}, Width: {width}")
    # print(f"Antennas: {antennas}")
    all_antennas = set()
    antinodes = set()
    all_antinodes = []
    for antenna, locations in antennas.items():
        # print(f"Antenna {antenna}: {locations}")
        new_antinodes = compute_antinodes(height, width, locations)
        antinodes |= new_antinodes
        all_antinodes.extend(list(new_antinodes))
        all_antennas |= locations

    return all_antennas, antinodes, all_antinodes


def part_2(mymap):
    height, width, antennas = decode_map(mymap)
    print(f"Height: {height}, Width: {width}")
    # print(f"Antennas: {antennas}")
    all_antennas = set()
    antinodes = set()
    all_antinodes = []
    for antenna, locations in antennas.items():
        # print(f"Antenna {antenna}: {locations}")
        new_antinodes = compute_antinodes(height, width, locations, full_line=True)
        antinodes |= new_antinodes
        all_antinodes.extend(list(new_antinodes))
        all_antennas |= locations

    return all_antennas, antinodes, all_antinodes


if __name__ == "__main__":
    with open("aoc_2024/adv08.txt", "r") as f:
        mymap = f.read().splitlines()
    all_antennas, antinodes, all_antinodes = part_1(mymap)
    print(f"Part 1: Number of antinodes: {len(antinodes)}")

    all_antennas, antinodes, all_antinodes = part_2(mymap)
    print(f"Part 2: Number of antinodes: {len(antinodes)}")
