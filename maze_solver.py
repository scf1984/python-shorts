from collections import deque


def solve_maze(maze, start, end):
    queue, visited = deque([[start]]), set()

    def is_valid_move(r, c):
        return 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == 0 and (r, c) not in visited

    while queue:
        *path, (curr_r, curr_c) = queue.pop()

        if (curr_r, curr_c) == end:
            return path + [(curr_r, curr_c)]

        visited.add((curr_r, curr_c))
        for row, col in ((curr_r + 1, curr_c), (curr_r - 1, curr_c), (curr_r, curr_c + 1), (curr_r, curr_c - 1)):
            if is_valid_move(row, col):
                queue.appendleft(path + [(curr_r, curr_c), (row, col)])


# Example usage
example_maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

print(solve_maze(example_maze, (0, 0), (4, 4)))
