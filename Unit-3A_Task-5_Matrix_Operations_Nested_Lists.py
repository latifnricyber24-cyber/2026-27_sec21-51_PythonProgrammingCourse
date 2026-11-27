a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

print("Addition:")
for i in range(2):
    for j in range(2):
        print(a[i][j] + b[i][j], end=" ")
    print()

print("Subtraction:")
for i in range(2):
    for j in range(2):
        print(a[i][j] - b[i][j], end=" ")
    print()
