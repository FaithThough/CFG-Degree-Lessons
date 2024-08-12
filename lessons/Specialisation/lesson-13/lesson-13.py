def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

def max_element(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

def print print_first_item(items):
    print(items[0])

def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            print(first_item, second_item)

def print_all_items_twice(items):
    for item in items:
        print(item)

    # again
    for item in items:
        print(item)

def print_first_item_then_first_half_then_say_hi_100_times(items):
    print(items[0])

    middle_index = len(items) // 2
    index = 0
    while index < middle_index:
        print(items[index])
        index += 1

    for time in range (100):
        print("hi")