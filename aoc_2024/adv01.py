import csv


def load_csv(f):
    reader = csv.reader(f, delimiter=" ", skipinitialspace=True)
    return list(map(list, zip(*[(int(x), int(y)) for (x, y) in reader])))


def compute_distances(a: list[int], b: list[int]) -> list[int]:
    return [abs(x[1] - x[0]) for x in list(zip(sorted(a), sorted(b)))]


def compute_similarities(a: list[int], b: list[int]) -> list[int]:
    return [x * len([y for y in b if y == x]) for x in a]


if __name__ == "__main__":
    filename = "tests/adv01.txt"
    print(f"Shall load file {filename}.")
    a, b = load_csv(open(filename, "r"))
    print(f"Loaded {len(a)}+{len(b)} elements.")

    distances = compute_distances(a, b)
    print(f"Sum of distances is {sum(distances)}.")

    similarities = compute_similarities(a, b)
    print(f"Sum of similarities is {sum(similarities)}.")
