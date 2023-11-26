def generate_pascals_triangle(n):
    triangle = row = []

    for i in range(n):
        row = [1 if j == 0 or j == i else row[j - 1] + row[j] for j in range(i + 1)]
        triangle.append(row)

    return triangle


def print_pascals_triangle(n):
    triangle = generate_pascals_triangle(n)
    max_width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        row_str = " ".join(map(str, row))
        spacing = (max_width - len(row_str)) // 2
        print(" " * spacing, end="")
        print(row_str)


print_pascals_triangle(5)
