def is_balanced_parentheses(s):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != closing_brackets[char]:
                return False
        # Ignore non-bracket characters

    return not stack  # The stack should be empty for balanced parentheses

expression1 = "({[()]})"
expression2 = "({[()})"
expression3 = "a + b * (c - d)"

print(f"Is '{expression1}' balanced? {is_balanced_parentheses(expression1)}")
print(f"Is '{expression2}' balanced? {is_balanced_parentheses(expression2)}")
print(f"Is '{expression3}' balanced? {is_balanced_parentheses(expression3)}")
