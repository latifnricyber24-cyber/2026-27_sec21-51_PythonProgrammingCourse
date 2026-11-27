n = int(input("Enter N: "))
total = 0
for i in range(n):
    num = int(input("Enter number: "))
    total += num
if n > 0:
    print("Sum =", total)
    print("Average =", total / n)
else:
    print("N must be positive") 
