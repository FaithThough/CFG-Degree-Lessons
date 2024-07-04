def is_within_range(num, _min, _max):
    """
    Check if a number is within a given range (inclusive).

    :param num: The number to check.
    :param _min: The minimum value of the range.
    :param _max: The maximum value of the range.
    :return: True if num is within the range, otherwise False.
    """
    if _min <= num <= _max:
        return True
    return False


def is_even(num):
    """
    Check if a number is even.

    :param num: The number to check.
    :return: True if num is even, otherwise False.
    """
    return num % 2 == 0


def red_or_blue(num):
    """
    Determine if a number should be classified as 'Red' or 'Blue'.

    :param num: The number to classify.
    :return: 'Red' or 'Blue' based on the given conditions.
    """
    if not is_even(num) or (is_even(num) and is_within_range(num, 6, 20)):
        return 'Red'

    if (is_even(num) and num > 20) or num in [2, 4]:
        return 'Blue'

def average_exam_score(student_marks):
    """
    Calculate the average exam score from a list of student marks.

    :param student_marks: A list of dictionaries with student marks.
    :return: The average score.
    :raises ValueError: If a mark is not within the valid range (2 to 9).
    """
    denominator = len(student_marks)
    marks = []

    for result in student_marks:
        try:
            mark = int(result['mark'])
        except KeyError:
            mark = 5  # Default mark if 'mark' key is missing

        if not 10 > mark > 1:
            raise ValueError("Mark value is not in the valid range")

        marks.append(mark)

    return sum(marks) / denominator

# Mocking
def get_file_content(file_name):
    """
    Read and return the content of a file as a list of lines.

    :param file_name: The name of the file to read.
    :return: A list of lines from the file.
    """
    with open(file_name, 'r') as file:
        return file.readlines()


def increment_line_number(file_name):
    """
    Increment the last line number from a file by 1.

    :param file_name: The name of the file to read.
    :return: The incremented line number.
    """
    content = get_file_content(file_name)
    num = int(content.pop().split('.')[0])
    return num + 1
