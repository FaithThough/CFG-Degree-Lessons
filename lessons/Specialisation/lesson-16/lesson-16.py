def find_three_highest_numbers(array):
    # Initialize variables to store the top three highest values
    highest = second_highest = third_highest = float('-inf')

    for num in array:
        if num > highest:
            # Update all three variables
            third_highest = second_highest
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            # Update second and third highest variables
            third_highest = second_highest
            second_highest = num
        elif num > third_highest and num != second_highest and num != highest:
            # Update third highest variable
            third_highest = num

    # Create the result list including duplicates if there are fewer than three unique values
    result = []
    if highest != float('-inf'):
        result.append(highest)
    if second_highest != float('-inf'):
        result.append(second_highest)
    if third_highest != float('-inf'):
        result.append(third_highest)

    # Fill in duplicates if necessary to ensure the result list has exactly three elements
    while len(result) < 3 and len(result) > 0:
        result.append(result[-1])

    return result

# Test cases
array1 = [141, 1, 18, -7, -17, -27, 18, 541, 8, 7, 7]
array2 = [8, 8, 8, 8, 8, 8, 8, 8, 10, 8, 8, 8, 8]
array3 = [1, 1, 1, 1, 1, 1, 1, 1]
array4 = [11, 4, 8, 11, 15]  # Example with duplicates

print("Result for array1:", find_three_highest_numbers(array1))  # Should be [541, 141, 18]
print("Result for array2:", find_three_highest_numbers(array2))  # Should be [10, 8, 8]
print("Result for array3:", find_three_highest_numbers(array3))  # Should be [1, 1, 1]
print("Result for array4:", find_three_highest_numbers(array4))  # Should be [15, 11, 11]

# Alternative solution
"""
EXAMPLE SOLUTION FOR 3 LARGEST NUMBERS WITHOUT SORTING

Check test cases below to test your code
"""


def find_3_largest_nums(array):
    three_largest = [None, None, None]
    for num in array:
        update_largest(three_largest, num)
    return three_largest


def update_largest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shift_n_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_n_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_n_update(three_largest, num, 0)


def shift_n_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]


#########################################################################

# Case 1, result = [18, 141, 541]

# array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
# print(find_3_largest_nums(array))

#####################################################

# Case 2, result = [8, 8, 10]
# array = [8, 8, 8, 8, 8, 8, 8, 8, 10, 8, 8, 8, 8, 8]
# print(find_3_largest_nums(array))

#####################################################

# Case 3, result = [1, 1, 1]
# array = [1, 1, 1, 1, 1, 1, 1, 1]
# print(find_3_largest_nums(array))

####################################################

# Case 4, result = [-2, -1, 7]
# array = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
# print(find_3_largest_nums(array))

####################################################