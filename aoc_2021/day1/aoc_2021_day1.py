def load_reports():
    with open("aoc_2021/day1/input.txt") as reports_file:
        return [int(report) for report in reports_file.readlines()]


def count_increased(reports):
    count = 0
    # print("{} (N/A - no previous measurement)".format(reports[0]))
    for i in range(1, len(reports)):
        if reports[i] > reports[i-1]:
            # print("{} (increased)".format(reports[i]))
            count += 1
        # else:
            # print("{} (decreased or equal)".format(reports[i]))

    return count


def count_increased_part2(reports):
    count = 0
    previous_swsum = swsum = reports[0] + reports[1] + reports[2]
    # print(f"{previous_swsum} (N/A - no previous sum)")
    for i in range(3, len(reports)):
        swsum = reports[i-2] + reports[i-1] + reports[i]

        if swsum > previous_swsum:
            # print(f"{swsum} (increased)")
            count += 1
        # else:
        #     print(f"{swsum} (decreased or equal)")

        previous_swsum = swsum

    return count


if __name__ == '__main__':
    reports = load_reports()
    print(f"Loaded {len(reports)} reports.")
    print("Number of increased reports: ", count_increased(reports))

    print("Number of increased reports (sliding window): ",
          count_increased_part2(reports))
