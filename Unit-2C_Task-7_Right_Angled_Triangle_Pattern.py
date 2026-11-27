n = int(input("Enter rows: "))
symbol = input("Enter symbol: ")
for i in range(1, n + 1):
    for j in range(i):
        print(symbol, end=" ")
    print()
