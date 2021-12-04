import unittest

from .aoc_2021_day3 import get_most_common_value, load_diagnostic_file, compute_ratings, compute_life_support_ratings, split_table_by_value_in_column

TEST_DIAGNOSTIC_REPORT = [
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
]

TEST_FILENAME = "aoc_2021/day3/test_input.txt"


class Test2021Day3(unittest.TestCase):
    def test_split_table_by_value_in_column(self):
        self.assertEqual(
            (
                5,
                7,
                [
                    [0, 0, 1, 0, 0],
                    [0, 1, 1, 1, 1],
                    [0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 1, 0],
                ],
                [
                    [1, 1, 1, 1, 0],
                    [1, 0, 1, 1, 0],
                    [1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 1]
                ]),
            split_table_by_value_in_column(0, TEST_DIAGNOSTIC_REPORT)
        )
        self.assertEqual(
            (
                7,
                5,
                [
                    [0, 0, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                ],
                [
                    [1, 1, 1, 1, 0],
                    [0, 1, 1, 1, 1],
                    [1, 1, 1, 0, 0],
                    [1, 1, 0, 0, 1],
                    [0, 1, 0, 1, 0],
                ]),
            split_table_by_value_in_column(1, TEST_DIAGNOSTIC_REPORT)
        )
        self.assertEqual(
            (
                2,
                0,
                [
                    [0],
                    [0]
                ],
                []
            ),
            split_table_by_value_in_column(0, [[0], [0]])
        )
        self.assertEqual(
            (
                1,
                1,
                [[0]],
                [[1]]
            ),
            split_table_by_value_in_column(0, [[0], [1]])
        )

    def test_get_most_common_value(self):
        self.assertEqual(
            1,
            get_most_common_value(0, TEST_DIAGNOSTIC_REPORT)
        )
        self.assertEqual(
            0,
            get_most_common_value(1, TEST_DIAGNOSTIC_REPORT)
        )
        self.assertEqual(
            0,
            get_most_common_value(0, [[0], [0]])
        )
        self.assertEqual(
            1,
            get_most_common_value(0, [[0], [1]])
        )

    def test_load_diagnostic_file(self):
        self.assertEqual(
            TEST_DIAGNOSTIC_REPORT,
            load_diagnostic_file(TEST_FILENAME)
        )

    def test_compute_ratings(self):
        self.assertEqual(
            (22, 9),
            compute_ratings(TEST_DIAGNOSTIC_REPORT)
        )

    def test_compute_life_support_ratings(self):
        self.assertEqual(
            (23, 10),
            compute_life_support_ratings(TEST_DIAGNOSTIC_REPORT)
        )


if __name__ == '__main__':
    unittest.main()
