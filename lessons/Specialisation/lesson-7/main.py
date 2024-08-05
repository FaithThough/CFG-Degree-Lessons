# itertools

import itertools

# Generate number starting from 10 and incrementing by 2
# Count()
counter = itertools.count(start=10, step=2)
print(next(counter))
print(next(counter))
print(next(counter))

# cycle
# cycles through an iterable indefinitely
colours = ["purple", "yellow", "pink"]
cycler = itertools.cycle(colours)
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))

# chain()
# combines multiple iterables into a single iterator
a = [1, 2, 3]
b = ["a", "b", "c"]
chained = itertools.chain(a, b)
print(list(chained))

# isslice
# isslice is an iterable to create a new iterable from a specific start, stop and step
# itertools.islice(iterable, start (inclusive), stop (exclusive)

numbers = itertools.count() # creates an infinite count starting from 0
sliced = itertools.islice(numbers, 10, 20) # takes a slice from the 10th to the 20th element
print(list(sliced)) # converts the slice to a list to see the elements

# Combinations
# Generates all possible combinations of a specified length from an iterable

letters = "ABC"
combination = itertools.combinations(letters, 2) # 2 is the length of the combination
print(list(combination))

# Permutations
# Generate all possible permutations of a specified length from an iterable
a = [1,2]
b  = ["a", "b"]
product = itertools.product(a,b)
print(list(product))

# repeat
# Repeats an object indefinitely or a specified number of times

repeated = itertools.repeat("CFG", 4)
print(list(repeated))

# compress
data = ["A", "B", "C", "D"]
selectors = [True, False, True, False]
compressed = itertools.compress(data, selectors)
print(list(compressed))

# dropwhile
# Drops elements from an iterable as long as a condition is true and then returns the rest
