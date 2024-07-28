import unittest

from lesson_29_team_challenge import minimum_waiting_time


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        patient_attend_times = [3, 2, 1, 2, 6]
        expected = 17
        actual = minimum_waiting_time(patient_attend_times)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        patient_attend_times = [2, 1, 1, 1]
        expected = 6
        actual = minimum_waiting_time(patient_attend_times)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        patient_attend_times = [1, 2, 4, 5, 2, 1]
        expected = 23
        actual = minimum_waiting_time(patient_attend_times)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        patient_attend_times = [25, 30, 2, 1]
        expected = 32
        actual = minimum_waiting_time(patient_attend_times)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        patient_attend_times = [1, 1, 1, 1, 1]
        expected = 10
        actual = minimum_waiting_time(patient_attend_times)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        patient_attend_times = [4, 3, 1, 1, 3, 2, 1, 8]
        expected = 45
        actual = minimum_waiting_time(patient_attend_times)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        patient_attend_times = [2]
        expected = 0
        actual = minimum_waiting_time(patient_attend_times)
        self.assertEqual(actual, expected)

    def test_case_8(self):
        patient_attend_times = [5, 4, 3, 2, 1]
        expected = 20
        actual = minimum_waiting_time(patient_attend_times)
        self.assertEqual(actual, expected)

    def test_case_9(self):
        patient_attend_times = [1, 2, 3, 4, 5]
        expected = 20
        actual = minimum_waiting_time(patient_attend_times)
        self.assertEqual(actual, expected)

    def test_case_10(self):
        patient_attend_times = [1, 1, 1, 4, 5, 6, 8, 1, 1, 2, 1]
        expected = 81
        actual = minimum_waiting_time(patient_attend_times)
        self.assertEqual(actual, expected)