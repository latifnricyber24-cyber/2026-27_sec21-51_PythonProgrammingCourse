
a = float(input("Enter principal amount: "))
b = float(input("Enter rate of interest: "))
c = float(input("Enter time in years: "))

amount = a * (1 + b / 100) ** c
ci = amount - a

print("Compound Interest =", round(ci, 2))
print("Total Amount =", round(amount, 2)) 