# Sample input
purple_hats_heights = [5, 8, 1, 3, 4]
black_hats_heights = [6, 9, 2, 4, 5]

print(sorted(purple_hats_heights))
print(sorted(black_hats_heights))

def can_take_picture(purple_hats_heights, black_hats_heights):
    purple_hats_heights.sort()
    black_hats_heights.sort()
    purple_hat_count = 0
    black_hat_count = 0
    array_length = len(purple_hats_heights)

    for i in range(len(purple_hats_heights)):
        if purple_hats_heights[i] > black_hats_heights[i]:
            purple_hat_count += 1
        elif black_hats_heights[i] > purple_hats_heights[i]:
            black_hat_count += 1

    if purple_hat_count == array_length:
        return True # Purple hats should be on the back row
    elif black_hat_count == array_length:
        return True # Black hats should be on the back row
    else:
        return False #The photo can't be taken

result = can_take_picture(purple_hats_heights, black_hats_heights)
print(f"Can the photo be taken: {result}")