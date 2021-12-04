import unittest

from .aoc_2021_day1 import count_increased, count_increased_part2


class Test2021Day1(unittest.TestCase):

    def test_count_increased(self):
        self.assertEqual(7, count_increased(
            [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))

    def test_count_increased_part2(self):
        self.assertEqual(5, count_increased_part2(
            [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))


if __name__ == '__main__':
    unittest.main()
