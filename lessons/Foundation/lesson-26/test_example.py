from unittest import TestCase, main, mock

from example import red_or_blue,average_exam_score, get_file_content, increment_line_number


class TestRedorBlueFunction(TestCase):
    """
    Unit tests for the red_or_blue function.
    """

    def test_even_in_range_2_to_5(self):
        """
        Test case for an even number within the range 2 to 5.
        Expected result is 'Blue'.
        """
        expected = 'Blue'
        result = red_or_blue(num=4)
        self.assertEqual(expected, result)

class TestAverageExamScore(TestCase):
    def test_calculate_average(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Chris', 'mark': 8},
            {'name': 'Lisa', 'mark': 6}
        ]
        expected = 7
        result = average_exam_score(my_input)
        self.assertEqual(expected, result)

class TestIncrementLineNumber(TestCase):
    """
    Unit tests for the increment_line_number function.
    """

    @mock.patch('example.get_file_content')
    def test_mock_file_read_function(self, mock_get_file_content):
        """
        Test case to check the increment_line_number function with mocked file content.
        Expected result is the next line number after the last number in the file.
        """
        content = [
            '1. Hello\n',
            '2. Hi\n',
            '3. Good morning\n',
        ]
        mock_get_file_content.return_value = content
        self.assertEqual(
            increment_line_number('some_file'),
            4
        )


if __name__ == "__main__":
    main()