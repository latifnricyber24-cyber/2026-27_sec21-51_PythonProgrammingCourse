n = int(input("Enter a number: "))
temp = n
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10
if 100 <= n <= 999 and total == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")
