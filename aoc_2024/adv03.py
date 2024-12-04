import re


def clean_input(input):
    r = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return [[int(m[0]), int(m[1])] for m in r.findall(input)]


def clean_input_adv(input):
    r = []
    r_do = re.compile(r"do\(\)")
    r_dont = re.compile(r"don't\(\)")
    r_mul = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    # split by do
    # then split the result by don't. take all matching from the first part
    for s_do in r_do.split(input):
        s_dont = r_dont.split(s_do)
        r.extend([[int(m[0]), int(m[1])] for m in r_mul.findall(s_dont[0])])
    return r


# on split par do() ou don't()

if __name__ == "__main__":
    filename = "aoc_2024/adv03.txt"
    print(f"Shall load file {filename}.")
    input = open(filename, "r").read()

    c = clean_input(input)
    print(f"Sum of mul of clean_input = {sum([x * y for (x, y) in c])}")
    c_adv = clean_input_adv(input)
    print(f"Sum of mul of adv_clean_input = {sum([x * y for (x, y) in c_adv])}")
