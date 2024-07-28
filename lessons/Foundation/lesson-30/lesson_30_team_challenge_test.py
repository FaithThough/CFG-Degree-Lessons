import unittest

from lesson_30_team_challenge import can_take_picture

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        purple_hats_heights = [10, 25, 30, 50, 40]
        black_hats_heights = [5, 20, 15, 45, 30]
        expected = True
        actual = can_take_picture(purple_hats_heights, black_hats_heights)
        self.assertEqual(actual, expected)
    def test_case_2(self):
        purple_hats_heights = [5, 20, 15, 45, 30]
        black_hats_heights = [10, 25, 30, 50, 40]
        expected = True
        actual = can_take_picture(purple_hats_heights, black_hats_heights)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        purple_hats_heights = [5, 5, 5gi, 5, 5]
        black_hats_heights = [5, 5, 5, 5, 5]
        expected = False
        actual = can_take_picture(purple_hats_heights, black_hats_heights)
        self.assertEqual(actual, expected)



