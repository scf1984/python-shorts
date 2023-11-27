def binary_to_decimal(binary_str):
    decimal_num = 0
    binary_str = binary_str[::-1]  # Reverse the binary string

    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            decimal_num += 2**i

    return decimal_num

# Example usage
binary_number1 = "1101"
binary_number2 = "101010"
binary_number3 = "11111111"

decimal_result1 = binary_to_decimal(binary_number1)
decimal_result2 = binary_to_decimal(binary_number2)
decimal_result3 = binary_to_decimal(binary_number3)

print(f"Binary {binary_number1} is equivalent to Decimal {decimal_result1}")
print(f"Binary {binary_number2} is equivalent to Decimal {decimal_result2}")
print(f"Binary {binary_number3} is equivalent to Decimal {decimal_result3}")
