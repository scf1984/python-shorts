def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

    return number == sum_of_powers

# Example usage
armstrong_number1 = 153
armstrong_number2 = 1634
non_armstrong_number = 123

print(f"Is {armstrong_number1} an Armstrong number? {is_armstrong_number(armstrong_number1)}")
print(f"Is {armstrong_number2} an Armstrong number? {is_armstrong_number(armstrong_number2)}")
print(f"Is {non_armstrong_number} an Armstrong number? {is_armstrong_number(non_armstrong_number)}")
