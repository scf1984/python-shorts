def queen_threatens(n, i, j):
    threatens = set()
    for k in range(n):
        threatens.update(((i, k), (k, j), (i - k, j - k), (i - k, j + k), (i + k, j - k), (i + k, j + k)))
    return threatens


def n_queens(n):
    available_squares = {(i, j) for i in range(n) for j in range(n)}
    placed_queens = []  # And the not-threatened squares they threaten!

    def solve():
        if len(placed_queens) == n:
            return placed_queens

        for square in available_squares:
            threatens = queen_threatens(n, *square) & available_squares
            available_squares.difference_update(threatens)
            placed_queens.append(square)
            solved = solve()
            if solved:
                return solved
            placed_queens.pop()
            available_squares.update(threatens)

    return solve()


print(n_queens(5))
