# # Tandem bicycle speed
# blue_shirts_speed = 8
# red_shirts_speed = 10
#
# tandem_speed = max(blue_shirts_speed, red_shirts_speed)
# print(tandem_speed)

red_riders = [5, 5, 3, 9, 2]
blue_riders = [3, 6, 7, 2, 1]

# Sort red_riders in descending order (highest to lowest)
red_riders.sort(reverse=True)

# Sort blue_riders in ascending order (lowest to highest)
blue_riders.sort()


def calculate_speed(fastest=True):
    if fastest:
        # Pair the highest red with the lowest blue for the fastest speed
        paired_speeds = [max(r, b) for r, b in zip(red_riders, blue_riders)]
    else:
        # Pair the highest red with the highest blue for the slowest speed
        paired_speeds = [max(r, b) for r, b in zip(red_riders, reversed(blue_riders))]

    return sum(paired_speeds)


# Calculate fastest and slowest speeds
fastest_speed = calculate_speed(fastest=True)
slowest_speed = calculate_speed(fastest=False)

# print(fastest_speed)  # Should print 32
# print(slowest_speed)  # Should print 25

def user_choice(fastest, slowest, fastest_parameter):
    return fastest if fastest_parameter else slowest

# Example usage of user_choice
fastest_result = user_choice(fastest_speed, slowest_speed, fastest_parameter=True)
slowest_result = user_choice(fastest_speed, slowest_speed, fastest_parameter=False)
print(fastest_result) # 32
print(slowest_result) # 25
