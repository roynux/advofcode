import csv


def load_reports(f):
    reader = csv.reader(f, delimiter=" ", skipinitialspace=True)
    return [list(map(int, row)) for row in reader]


def is_report_safe(levels) -> bool:
    # print(levels)
    previous_level = levels[0]
    previous_diff = 0
    for i in range(1, len(levels)):
        diff = levels[i] - previous_level
        # print(
        #     f"previous_level={previous_level}, previous_diff={previous_diff}, i={i}, levels[i]={levels[i]}, diff={diff}"
        # )
        if diff == 0 or abs(diff) > 3:
            return False
        if diff * previous_diff < 0:
            return False
        previous_diff = diff
        previous_level = levels[i]
    return True


def is_report_safe_tolerance(levels) -> bool:
    for i in range(len(levels)):
        l = levels.copy()
        l.pop(i)
        if is_report_safe(l):
            return True

    return False


if __name__ == "__main__":
    filename = "aoc_2024/adv02.txt"
    print(f"Shall load file {filename}.")
    reports = load_reports(open(filename, "r"))
    print(f"Loaded {len(reports)} reports.")

    safe_reports_count = len([True for levels in reports if is_report_safe(levels)])
    print(f"Number of safe reports: {safe_reports_count}.")

    safe_reports_tol_count = len(
        [True for levels in reports if is_report_safe_tolerance(levels)]
    )
    print(f"Number of safe reports with tolerance: {safe_reports_tol_count}.")
