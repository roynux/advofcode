from aoc_2024.adv03 import clean_input, clean_input_adv


def test_clean_input():
    sample1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert clean_input(sample1) == [[2, 4], [5, 5], [11, 8], [8, 5]]
    sample2 = "mul(999,0)mul(-1,5)mul(1000,5)"
    assert clean_input(sample2) == [[999, 0]]

    assert (
        sum([x * y for (x, y) in clean_input(sample1)])
        == 2 * 4 + 5 * 5 + 11 * 8 + 8 * 5
    )


def test_clean_input_adv():
    sample1 = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    assert clean_input_adv(sample1) == [[2, 4], [8, 5]]
