small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99)  # Does not throw an error if value is not found
print(small_ints)

small_ints.remove(99)  # throws an error if the value is not found
print(small_ints)


