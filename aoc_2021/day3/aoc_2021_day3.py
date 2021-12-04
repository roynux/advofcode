DATA_FILE = "aoc_2021/day3/input.txt"


def get_most_common_value(col, table):
    nbr_rows = len(table)
    t = 0
    for r in range(nbr_rows):
        t += table[r][col]
    return 1 if t >= nbr_rows / 2 else 0


def split_table_by_value_in_column(col, table):
    nbr_rows = len(table)
    rows_0 = []
    rows_1 = []
    t = 0
    for r in range(nbr_rows):
        if table[r][col]:
            t += table[r][col]
            rows_1.append(table[r])
        else:
            rows_0.append(table[r])
    most_common_value = 1 if t >= nbr_rows / 2 else 0
    return nbr_rows - t, t, rows_0, rows_1


def load_diagnostic_file(filename):
    with open(filename) as f:
        return [
            [int(e) for e in line.strip()] for line in f.readlines()
        ]


def compute_ratings(diagnostic_report):
    gamma_rate = 0
    epsilon_rate = 0
    nbr_reports = len(diagnostic_report)
    for col in range(len(diagnostic_report[0])):
        b = get_most_common_value(col, diagnostic_report)
        gamma_rate = gamma_rate * 2 + b
        epsilon_rate = epsilon_rate * 2 + (0 if b else 1)
        # print(f"col: {col} t: {t} b: {b} gamma_rate: {gamma_rate}")
    return gamma_rate, epsilon_rate


def compute_life_support_ratings(diagnostic_report):
    oxygen_rate = 0
    co2_rate = 0
    table = diagnostic_report
    for col in range(len(diagnostic_report[0])):
        count_0, count_1, rows_0, rows_1 = split_table_by_value_in_column(
            col, table)

        table = rows_1 if count_1 >= count_0 else rows_0

    for e in table[0]:
        oxygen_rate = oxygen_rate * 2 + e

    table = diagnostic_report
    nbr_cols = len(diagnostic_report[0])
    col = 0
    while col < nbr_cols and len(table) > 1:
        count_0, count_1, rows_0, rows_1 = split_table_by_value_in_column(
            col, table)

        table = rows_0 if count_0 <= count_1 else rows_1
        col += 1

    for e in table[0]:
        co2_rate = co2_rate * 2 + e

    return oxygen_rate, co2_rate


if __name__ == "__main__":
    diagnostic_report = load_diagnostic_file(DATA_FILE)
    gamma_rate, epsilon_rate = compute_ratings(diagnostic_report)
    print(
        f"gamma_rate: {gamma_rate}, epsilon_rate: {epsilon_rate} submarine consumption: {gamma_rate * epsilon_rate}")

    oxygen_rate, co2_rate = compute_life_support_ratings(diagnostic_report)
    print(
        f"oxygen_rate: {oxygen_rate}, co2_rate: {co2_rate} submarine consumption: {oxygen_rate * co2_rate}")
