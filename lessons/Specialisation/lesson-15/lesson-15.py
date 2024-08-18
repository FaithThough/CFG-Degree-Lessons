# # Linear search
#
# # Bubble sort
# def bubble_sort(array_of_numbers):
#     n = len(array_of_numbers)
#     for i in range (n): # iterate through the list multiple times, responsible for comparing adjacent elements and performing swaps if they're in the wrong order
#         for j in range(0, n-i-1):
#             if array_of_numbers[j] > array_of_numbers[j+1]:
#                 array_of_numbers[j], array_of_numbers[j+1] = array_of_numbers[j+1], array_of_numbers[j] # Swapping the numbers
#
#     return array_of_numbers
#
# array = [64, 34, 25, 12, 22, 11, 90]
# sorted_array = bubble_sort(array)
# print(f"Sorted array: {sorted_array}")

# # Selection sort
# def selection_sort(array_of_numbers):
#     for i in range (len(array_of_numbers)):
#         minimum_index = i
#         for j in range(i+1, len(array_of_numbers)):
#             if array_of_numbers[j] < array_of_numbers[minimum_index]:
#                 minimum_index = j
#         array_of_numbers[i], array_of_numbers[minimum_index] = array_of_numbers[minimum_index], array_of_numbers[i]
#
# array = [64, 34, 25, 12, 22, 11, 90]
# selection_sort(array)
# print(array)

# Insertion sort
def insertion_sort(array_of_numbers):
    for i in range(1, len(array_of_numbers)): # We're assuming that the first item is already sorted
        key = array_of_numbers[i] # Stores the current element at index i in the variable key. The key will be compared with the element in the sorted portion of the array.
        j = i - 1 # This is the index from the last element in the sorted portion of the array.
        while j >= 0 and key < array_of_numbers[j]: # j >= 0 Ensures that the loop doesn't go out of bounds and doesn't compare with elements that don't exist. key < array_of_numbers[j] Checks that the key is smaller than the current element and if so then the key needs to be inserted at the earlier position
            array_of_numbers[j + 1] = array_of_numbers[j] # If the condition is true the array line shifts array one position to the right(?)
            j -= 1 # Decreasing j by 1, moving the comparison to the next element to the left in the array
            # The loop will continue to shift to the right as long as the key is smaller than the array j
            array_of_numbers[j + 1] = key

array = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(array)
print(array)





