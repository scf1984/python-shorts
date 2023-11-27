def n_queens(n):
    available_squares = {(i, j)
                         for i in range(n)
                         for j in range(n)}
    placed_queens = []

    def get_threatened_squares(queen_square):
        i, j = queen_square
        for k in range(n):
            for square in ((i, k), (i - k, j - k),
                           (i - k, j + k), (i + k, j - k),
                           (i + k, j + k), (k, j)):
                if square in available_squares:
                    yield square

    def solve(col=0):
        if len(placed_queens) == n:
            yield tuple(placed_queens)

        for square in set(zip(range(n), [col] * n)) & available_squares:
            threatens = set(get_threatened_squares(square))

            available_squares.difference_update(threatens)
            placed_queens.append(square)

            solution = solve(col + 1)
            if solution:
                yield from solution

            placed_queens.pop()
            available_squares.update(threatens)

    yield from solve()


print(len([*n_queens(8)]))
