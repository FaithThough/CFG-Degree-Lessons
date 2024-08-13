# For our practice today we are going to look at few solutions to common Python algorithms
# that are frequently asked problems in coding interview rounds.

# 1. Checking for Anagrams
# This algorithm checks if two strings are anagrams of each other.
# 1. Start
# 2. Declare two variables, `string_one` and `string_two`.
# 3. Check the length of `string_one` and `string_two`:
#     - If the lengths are not the same, return "fail" (the strings cannot be anagrams).
#     - If the lengths are the same, proceed to the next step.
# 4. Sort the characters in both `string_one` and `string_two`.
# 5. Compare the sorted versions of `string_one` and `string_two`:
#     - If they are identical, return "pass" (the strings are anagrams).
#     - If they are not identical, return "fail" (the strings are not anagrams).
# 6. Stop

def check_anagram(string_one, string_two):
    # Convert strings to lowercase
    string_one = string_one.lower()
    string_two = string_two.lower()

    # Check if lengths are different
    if len(string_one) != len(string_two):
        return "Fail"

    # Sort the characters in both strings
    sorted_string_one = sorted(string_one)
    sorted_string_two = sorted(string_two)

    # Compare the sorted strings
    if sorted_string_one == sorted_string_two:
        return "Pass"
    else:
        return "Fail"

string_one = "silent"
string_two = "listen"

result = check_anagram(string_one, string_two)
print(result)


# ###################################################################
# # 2. Average Words Length
#
# # For a given sentence, return the average word length.
# # Note: Remember to remove punctuation first.
#
# sentence1 = "Hi class, we are practicing solving algorithms. It is fun, don't you think?.."
# sentence2 = "We need to work very hard to learn more about algorithms!"

# 1. Start
# 2. Declare a variable, `sentence`, and assign it the sentence for which you want to calculate the average word length (e.g., `sentence1` or `sentence2`).
# 3. Remove all punctuation characters from the `sentence`.
# 4. Split the `sentence` into individual words.
# 5. Count the total number of characters in the sentence (excluding spaces).
# 6. Count the total number of words in the sentence.
# 7. Divide the total number of characters by the total number of words to calculate the average word length.
# 8. Return the average word length.
# 9. Stop
import string

def average_word_length(sentence):
    # Remove punctuation from the sentence
    stripped_sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    # # Debugging: Print stripped sentence
    # print("Stripped Sentence:", stripped_sentence)

    # Split the sentence into words based on spaces
    split_sentence = stripped_sentence.split()

    # # Debugging: Print split sentence (list of words)
    # print("Split Sentence:", split_sentence)

    # Calculate the total number of characters in all words
    character_count = sum(len(word) for word in split_sentence)

    # # Debugging: Print total character count
    # print("Character Count:", character_count)

    # Calculate the total number of words
    word_count = len(split_sentence)

    # # Debugging: Print word count
    # print("Word Count:", word_count)

    # Compute the average word length
    if word_count == 0:
        return 0  # Return 0 if there are no words to avoid division by zero
    average_length = character_count / word_count
    # Round to two decimal places
    return round(average_length, 2)


# Example usage
sentence1 = "Hi class, we are practicing solving algorithms. It is fun, don't you think?.."
sentence2 = "We need to work very hard to learn more about algorithms!"

print("Average Word Length for Sentence 1:", average_word_length(sentence1))
print("Average Word Length for Sentence 2:", average_word_length(sentence2))

# ###################################################################
# # 3. Move zeros
#
# # Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# # the non-zero elements.
#
# array1 = [0, 1, 0, 3, 12]  # --> should be [1, 3, 12, 0, 0]
# array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]  # --> should be [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

# 1. Start
# 2. Set a position marker**: Create a position marker named `last_non_zero_index` and set it to 0. This marker helps us know where to place the next non-zero number.
# 3. Look at each number: Go through each number in the array one by one.
# - If the number is not zero:
#     - Move this number to the position marked by `last_non_zero_index`.
#     - Move the position marker (`last_non_zero_index`) one place forward.
# 4. Fill remaining places with zeros: After you have placed all non-zero numbers, fill the rest of the array (from the current position of `last_non_zero_index` to the end) with zeros.
# 5. Stop

def move_zeros(array):
    last_non_zero_index = 0

    for i in range(len(array)):
        if array[i] != 0:
            # Swap non-zero element with the element at last_non_zero_index
            array[last_non_zero_index], array[i] = array[i], array[last_non_zero_index]
            last_non_zero_index += 1  # Move the index for the next non-zero element

    return array

array1 = [0, 1, 0, 3, 12]  # [1, 3, 12, 0, 0]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]  #[1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

print(move_zeros(array1))
print(move_zeros(array2))