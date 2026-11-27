n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
if n >= 0:
    print("Factorial =", fact)
else:
    print("Factorial not defined")
