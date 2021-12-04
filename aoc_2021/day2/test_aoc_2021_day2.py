import unittest

from .aoc_2021_day2 import dive, dive_with_aim, to_command


class Test2021Day2(unittest.TestCase):

    def test_to_command(self):
        self.assertEqual(to_command('forward 5\n'), ["forward", 5])

    def test_assert_dive(self):
        self.assertEqual(dive([["forward", 5], ["down", 5], ["forward", 8], [
            "up", 3], ["down", 8], ["forward", 2]]), (15, 10))

    def test_assert_dive_with_aim(self):
        self.assertEqual(dive_with_aim([["forward", 5], ["down", 5], ["forward", 8], [
            "up", 3], ["down", 8], ["forward", 2]]), (15, 60))


if __name__ == '__main__':
    unittest.main()
