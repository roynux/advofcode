import operator


def split_equation_lines(equation_lines):
    for line in equation_lines:
        parts = line.split(":")
        if len(parts) != 2:
            raise ValueError(f"Invalid line format: {line}")
        yield (int(parts[0]), [int(x) for x in parts[1].split()])


def compute_combinations(operators, results, acc, vals):
    if len(vals):
        for op in operators:
            compute_combinations(operators, results, op(acc, vals[0]), vals[1:])
    else:
        results.append(acc)


def part_1(data):
    r = 0
    for expected_result, values in split_equation_lines(data):
        operators = [operator.add, operator.mul]
        results = []
        compute_combinations(operators, results, values[0], values[1:])
        r += (
            expected_result
            if any([True for x in results if x == expected_result])
            else 0
        )
    return r


# import math


def my_concat(a, b):
    return int(str(a) + str(b))
    # return a * (int(math.ceil(math.log10(b))) + 1) + b


def part_2(data):
    r = 0
    for expected_result, values in split_equation_lines(data):
        operators = [operator.add, operator.mul, my_concat]
        results = []
        compute_combinations(operators, results, values[0], values[1:])
        r += (
            expected_result
            if any([True for x in results if x == expected_result])
            else 0
        )
    return r


if __name__ == "__main__":
    with open("aoc_2024/adv07.txt", "r") as f:
        data = f.read().splitlines()
    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")
