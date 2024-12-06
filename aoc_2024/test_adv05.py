import pytest

# a doit être avant b
# 29|13
# 47|13,29,53,61
# 53|13,29
# 61|13,29,53
# 75|13,29,47,53,61
# 97|13,29,47,53,61,75

# a doit être après b
# 13:29,47,53,61,75,97
# 29:47,53,61,75,97
# 47:75,97
# 53:47,61,75,97
# 61:47,75,97
# 75:97


@pytest.fixture
def fixture_rules():
    return """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
"""


@pytest.fixture
def fixtures_updates_list():
    return """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def load_rules_before(rules_text):
    r = {}
    for row in rules_text.split():
        a, b = list(map(int, row.split("|")))
        if a in r:
            r[a] = r[a] | {b}
        else:
            r[a] = {b}
    return r


def load_rules_after(rules_text):
    r = {}
    for row in rules_text.split():
        a, b = list(map(int, row.split("|")))
        if b in r:
            r[b] = r[b] | {a}
        else:
            r[b] = {a}
    return r


def test_load_rules_before(fixture_rules):
    assert load_rules_before(fixture_rules) == {
        29: {13},
        47: {13, 29, 53, 61},
        53: {13, 29},
        61: {13, 29, 53},
        75: {13, 29, 47, 53, 61},
        97: {13, 29, 47, 53, 61, 75},
    }


def test_load_rules_after(fixture_rules):
    assert load_rules_after(fixture_rules) == {
        13: {29, 47, 53, 61, 75, 97},
        29: {47, 53, 61, 75, 97},
        47: {75, 97},
        53: {47, 61, 75, 97},
        61: {47, 75, 97},
        75: {97},
    }


def are_updates_valid(updates_line,rules_before, rules_after) -> bool:
    updates = list(map(int, updates_line.split(",")))
    for i, update in enumerate(updates):
        if update in rules_before:
            # check that updates before current are not in the rules_BEFORE
    return True


def test_updates_valid(fixture_rules):
    rules_before = load_rules_before(fixture_rules)
    rules_after = load_rules_after(fixture_rules)
    assert are_updates_valid("75,47,61,53,29", rules_before, rules_after) == True
