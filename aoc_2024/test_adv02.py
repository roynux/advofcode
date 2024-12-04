import csv
from io import StringIO
import pytest

from aoc_2024.adv02 import is_report_safe, load_reports, is_report_safe_tolerance


@pytest.fixture
def get_list_fixture():
    return """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def test_adv02(get_list_fixture):
    reports = load_reports(StringIO(get_list_fixture))
    assert reports == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]

    # assert is_report_safe(reports[0]) == True
    # assert is_report_safe(reports[1]) == False
    # assert is_report_safe(reports[2]) == False
    # assert is_report_safe(reports[3]) == False
    # assert is_report_safe(reports[4]) == False
    # assert is_report_safe(reports[5]) == True

    # assert len([True for report in reports if is_report_safe(report)]) == 2

    assert is_report_safe_tolerance(reports[0]) == True
    assert is_report_safe_tolerance(reports[1]) == False
    assert is_report_safe_tolerance(reports[2]) == False
    assert is_report_safe_tolerance(reports[3]) == True
    assert is_report_safe_tolerance(reports[4]) == True
    assert is_report_safe_tolerance(reports[5]) == True

    assert is_report_safe(levels=[72, 76, 79, 80, 83, 85, 87, 90]) == False
    assert is_report_safe_tolerance(levels=[72, 76, 79, 80, 83, 85, 87, 90]) == True
    assert is_report_safe_tolerance(levels=[82, 84, 85, 87, 90, 92, 93, 91]) == True
    assert is_report_safe_tolerance(levels=[7, 10, 12, 14, 17, 19, 22, 22]) == True
    assert is_report_safe_tolerance(levels=[66, 68, 69, 72, 74, 78]) == True
    assert is_report_safe_tolerance(levels=[10, 11, 13, 14, 17, 18, 25]) == True

    assert len([True for report in reports if is_report_safe_tolerance(report)]) == 4
    # assert 0 == 1
