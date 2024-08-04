# Iterators are objects that can be iterated upon

# numbers = [2,4,1,9,6] # iterable, can be looped over

# methods = dir(numbers)
# for m in methods:
#     print (m)

# for number in numbers:
#     print(number)


# numbers_iterated = iter(numbers) # iter function is used to create an iterator from the iterable
#
# print(numbers_iterated)
#
# print(next(numbers_iterated))
# print(next(numbers_iterated))
# print(next(numbers_iterated))
# print(next(numbers_iterated))
# print(next(numbers_iterated))
# # print(next(numbers_iterated)) # will raise a StopIteration exception because there are no numbers left

# Generators
# Simple generator function
# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#
# generate = simple_generator()
# print(next(generate))
# print(next(generate))
# print(next(generate))
# print(next(generate))


# # Infinite sequence
# def infinite_counter():
#     count = 0
#     while True:
#         yield count
#         count +=1
#
# counter = infinite_counter()
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
# # Creating an iterator
#
# class EvenNumbers:
#     def __iter__(self):
#         self.number = 0
#         return self
#
#     def __next__(self):
#         next_number = self.number
#         self.number += 2
#         return next_number
#
# # Usage
# even_numbers = EvenNumbers()
# iterator = iter(even_numbers)
#
# print(next(iterator))  # Output: 0
# print(next(iterator))  # Output: 2
# print(next(iterator))  # Output: 4
# print(next(iterator))  # Output: 6
#
# class EvenNumbersUpToTen:
#     def __iter__(self):
#         self.number = 0
#         return self
#
#     def __next__(self):
#         if self.number < 10:
#             next_number = self.number
#             self.number += 2
#             return next_number
#         else:
#             raise StopIteration
#
# even_numbers = EvenNumbersUpToTen()
# even_iter = iter(even_numbers)
#
# print(next(even_iter))
# print(next(even_iter))
# print(next(even_iter))
# print(next(even_iter))
# print(next(even_iter))
# print(next(even_iter))  # This will raise StopIteration

class PowerThreeSequence:
    def __init__(self, max_times=0):
        self.number = 0
        self.max = max_times

    def __iter__(self):
        return self

    def __next__(self):
        if self.number >= self.max:
            raise StopIteration
        result = 3 ** self.number
        self.number += 1
        return result

power_three_sequence = PowerThreeSequence(max_times=5)
power_three_iter = iter(power_three_sequence)

print(next(power_three_iter))
print(next(power_three_iter))
print(next(power_three_iter))
print(next(power_three_iter))
print(next(power_three_iter))
print(next(power_three_iter))