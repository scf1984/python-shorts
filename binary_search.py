from bisect import bisect_left


def binary_search(arr, target):
    index = bisect_left(arr, target)
    if index != len(arr) and arr[index] == target:
        return index
    raise ValueError


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
