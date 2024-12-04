def find_xmas(d):
    w = len(d[0]) + 6
    data = ["." * w] * 3 + ["..." + row + "..." for row in d] + ["." * w] * 3
    # find XMAS
    height = len(data)
    width = len(data[0])
    print(height, width)
    acc = 0
    for y in range(height):
        for x in range(width):
            if data[y][x] == "X":
                print(f"y={y} x={x}")

                e = data[y][x : x + 4]
                print(f"e={e}")

                se = (
                    data[y][x]
                    + data[y + 1][x + 1]
                    + data[y + 2][x + 2]
                    + data[y + 3][x + 3]
                )
                print(f"se={se}")

                s = data[y][x] + data[y + 1][x] + data[y + 2][x] + data[y + 3][x]
                print(f"s={s}")

                so = (
                    data[y][x]
                    + data[y + 1][x - 1]
                    + data[y + 2][x - 2]
                    + data[y + 3][x - 3]
                )
                print(f"so={so}")

                o = data[y][x - 3 : x + 1]
                print(f"o={o}")

                no = (
                    data[y][x]
                    + data[y - 1][x - 1]
                    + data[y - 2][x - 2]
                    + data[y - 3][x - 3]
                )
                print(f"no={no}")

                n = data[y][x] + data[y - 1][x] + data[y - 2][x] + data[y - 3][x]
                print(f"n={n}")

                ne = (
                    data[y][x]
                    + data[y - 1][x + 1]
                    + data[y - 2][x + 2]
                    + data[y - 3][x + 3]
                )
                print(f"ne={ne}")

                for words in [n, ne, e, se, s, so, o, no]:
                    if words in ["XMAS", "SAMX"]:
                        acc += 1
    return acc


def find_mas(d):
    w = len(d[0]) + 6
    data = ["." * w] * 3 + ["..." + row + "..." for row in d] + ["." * w] * 3
    # find MAS
    height = len(data)
    width = len(data[0])
    print(height, width)
    acc = 0
    for y in range(height):
        for x in range(width):
            if data[y][x] == "A":
                print(f"y={y} x={x}")
                l = data[y - 1][x - 1] + data[y][x] + data[y + 1][x + 1]
                r = data[y - 1][x + 1] + data[y][x] + data[y + 1][x - 1]

                if l in ["MAS", "SAM"] and r in ["MAS", "SAM"]:
                    acc += 1
                    print("Found word ", acc)
    return acc


if __name__ == "__main__":
    data = open("aoc_2024/adv04.txt", "r").readlines()
    print(f"Found XMAS {find_xmas(data)} in file.")
    print(f"Found MAS {find_mas(data)} in file.")
