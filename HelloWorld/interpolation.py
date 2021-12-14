age = 24
print("My age is %d years" % age)
# %f = float
# %s = string
# %d = number

major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("PI is approximately %f" % (22/7))
print("PI is approximately %60.50f" % (22/7))


data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])
