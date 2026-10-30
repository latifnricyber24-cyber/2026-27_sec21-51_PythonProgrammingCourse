a = 10
b = 5
c = 2

result = a + b * c
print("Operator precedence:", result)

result = (a + b) * c
print("Using parentheses:", result)

result = a - b - c
print("Left to right associativity:", result)

result = 2 ** 3 ** 2
print("Right to left associativity:", result)