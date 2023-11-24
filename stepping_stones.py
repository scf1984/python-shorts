#  Can a 2-path stones pattern be traversed from first to last? (start from path 1)
# 1: --------              -----    ---
# 2:      ------------------  -----------
# Yes!


# 1: --------              -----    ---
# 2:      -----    --------  -----------
# No!

def stepping_stones(path_1: list[tuple[int, int]], path_2: list[tuple[int, int]], current_step=None):
    if current_step is None:
        return stepping_stones(path_2, path_1, path_1.pop(0))

    if not path_1 and not path_2:
        return True

    while path_1 and path_1[0][1] <= current_step[1]:
        path_1.pop(0)

    if path_1 and path_1[0][0] <= current_step[1] <= path_1[0][1]:
        return stepping_stones(path_2, path_1, path_1.pop(0))

    return False


print(stepping_stones([(0, 10), (12, 15), (50, 70)], [(8, 12), (14, 100), (120, 150)])) # False
print(stepping_stones([(0, 10), (12, 15), (50, 130)], [(8, 12), (14, 100), (120, 150)])) # True