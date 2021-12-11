a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)    # division produces a float result
print(a // b)   # integer division, rounded down towards minus infinity
print(a % b)    # module: the remainder after integer division

print()

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))

# TO get  12
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()
print(a / (b * a) / b)
