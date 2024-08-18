# Loop
def print_numbers_with_loop():
    for i in range (1, 11):
        print(i)

print_numbers_with_loop()

# Recursion
def print_numbers_with_recursion(n=1):
    if n > 10:
        return
    print(n)
    print_numbers_with_recursion(n + 1)

print_numbers_with_recursion()

# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

Fibonacci sequence
 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

def fibonacci_number(n):
    if n <=1:
        return n
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)

print(fibonacci_number(7))

def fibonacci_sequence(n):
    def generate_fibonacci_sequence(a, b, count, result):
        if count < n:
            result.append(a)
            generate_fibonacci_sequence(b, a + b, count + 1, result)

    sequence = []
    generate_fibonacci_sequence(0, 1, 0, sequence)
    return sequence

print(fibonacci_sequence(5))  # Output: [0, 1, 1, 2, 3]

"""
Return all possible combination of strings of given length,
which can be formed from a set of supplied characters.

Input:
char_set = {'a', 'b'}, length = 3

Output:
aaa
aab
aba
abb
baa
bab
bba
bbb

BV: we can't use intertools product or permutation functions
"""

def get_string_combinations(char_set, l):
    n = len(char_set)
    get_string_combinations_rec(char_set,"", n, l) # primary function to be called to get all possible combinations of strings for a specified length

def get_string_combinations_rec(char_set, prefix, n, l):
    if l == 0:
        print(prefix)
        return
    for i in range(n):
        new_prefix = prefix + char_set[i]
        get_string_combinations_rec(char_set, new_prefix, n, l-1)

set1 = ['a', 'b']
k = 3
get_string_combinations(set1, k)



