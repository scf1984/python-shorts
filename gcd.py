def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(calculate_gcd(12, 24))
