age = 24
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

# replacement fields don't have to be specified in order.
# The number determines what value to use.
# the replacement field can be used more than once
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}".format(28,30,31))
print()
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
""".format(28, 30, 31))


