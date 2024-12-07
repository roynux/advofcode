import pytest
from aoc_2024.adv05 import (
    compute_updates,
    is_update_valid,
    load_data,
    correct_pages_order,
    compute_corrected_updates,
)


@pytest.fixture
def fixture_data():
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

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def test_load_data(fixture_data):
    assert load_data(fixture_data) == (
        {
            29: {13},
            47: {13, 29, 53, 61},
            53: {13, 29},
            61: {13, 29, 53},
            75: {13, 29, 47, 53, 61},
            97: {13, 29, 47, 53, 61, 75},
        },
        {
            13: {29, 47, 53, 61, 75, 97},
            29: {47, 53, 61, 75, 97},
            47: {75, 97},
            53: {47, 61, 75, 97},
            61: {47, 75, 97},
            75: {97},
        },
        [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13],
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47],
        ],
    )


def test_updates_valid(fixture_data):
    rules_before, rules_after, updates_list = load_data(fixture_data)
    assert is_update_valid(updates_list[0], rules_before, rules_after) is True
    assert is_update_valid(updates_list[1], rules_before, rules_after) is True
    assert is_update_valid(updates_list[2], rules_before, rules_after) is True
    assert is_update_valid(updates_list[3], rules_before, rules_after) is False
    assert is_update_valid(updates_list[4], rules_before, rules_after) is False
    assert is_update_valid(updates_list[5], rules_before, rules_after) is False


def test_correct_pages_order(fixture_data):
    rules_before, rules_after, updates_list = load_data(fixture_data)
    assert correct_pages_order([75, 97, 47, 61, 53], rules_before, rules_after) == [
        97,
        75,
        47,
        61,
        53,
    ]
    assert correct_pages_order([61, 13, 29], rules_before, rules_after) == [
        61,
        29,
        13,
    ]
    assert correct_pages_order([97, 13, 75, 29, 47], rules_before, rules_after) == [
        97,
        75,
        47,
        29,
        13,
    ]


def test_compute_updates(fixture_data):
    rules_before, rules_after, updates_list = load_data(fixture_data)
    assert compute_updates(rules_before, rules_after, updates_list) == 143


def test_compute_corrected_updates(fixture_data):
    rules_before, rules_after, updates_list = load_data(fixture_data)
    assert compute_corrected_updates(rules_before, rules_after, updates_list) == 123
