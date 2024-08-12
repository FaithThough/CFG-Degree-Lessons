# # Loop
# def print_numbers_with_loop():
#     for i in range (1, 11):
#         print(i)
#
# print_numbers_with_loop()

# Recursion
def print_numbers_with_recursion(n=1):
    if n > 10:
        return
    print(n)
    print_numbers_with_recursion(n + 1)

print_numbers_with_recursion()