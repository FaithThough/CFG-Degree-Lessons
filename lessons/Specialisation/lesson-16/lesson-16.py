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
