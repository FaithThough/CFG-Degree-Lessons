# Palindrome
# Checking whether strings are palindrome or not
def is_palindrome(s):
    lower = s.lower()
    return lower == s[::-1] #reversing everything and then comparing

string = "wrtfawmnoonmz"

min_length = 1
max_length = len(string)

substrings = [string[i:i+j] for i in range(len(string)-min_length) for j in range(min_length, max_length+1)]
print(substrings)
# sorted_substrings = sorted(substrings, key=len, reverse=True)
# print (sorted_substrings)

longest_palindrome = ""

def does_palindrome_substring_exist():
    global longest_palindrome
    sorted_substrings = sorted(substrings, key=len, reverse=True)
    for i in range(len(sorted_substrings)):
        if is_palindrome(sorted_substrings[i]):
            longest_palindrome = sorted_substrings[i]
            return True
    return False

if does_palindrome_substring_exist():
    print(f"Longest palindrome is {longest_palindrome}")
else:
    print(f"No palindrome found")

