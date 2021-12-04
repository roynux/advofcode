def to_command(line):
    e = line.strip().split(" ")
    return [e[0], int(e[1])]


def dive(commands):
    horizontal_position = 0
    depth = 0
    for command in commands:
        # print(command)
        if command[0] == "forward":
            horizontal_position += command[1]
        elif command[0] == "up":
            depth -= command[1]
        elif command[0] == "down":
            depth += command[1]
    # print(f"horizontal_position: {horizontal_position}, depth: {depth}")

    return horizontal_position, depth


def dive_with_aim(commands):
    horizontal_position = 0
    depth = 0
    aim = 0
    for command in commands:
        # print(command)
        if command[0] == "forward":
            horizontal_position += command[1]
            depth += aim * command[1]
        elif command[0] == "up":
            aim -= command[1]
        elif command[0] == "down":
            aim += command[1]
    print(
        f"horizontal_position: {horizontal_position}, depth: {depth}, aim: {aim}")

    return horizontal_position, depth


def load_input():
    with open("aoc_2021/day2/input.txt") as f:
        return [to_command(line) for line in f.readlines()]


if __name__ == "__main__":
    commands = load_input()

    print(f"Loaded {len(commands)} commands.")
    horizontal_position, depth = dive(commands)
    print(
        f"Dived to horizontal_position: {horizontal_position} * depth: {depth} = {horizontal_position * depth}")

    horizontal_position, depth = dive_with_aim(commands)
    print(
        f"Dived with aim to horizontal_position: {horizontal_position} * depth: {depth} = {horizontal_position * depth}")
