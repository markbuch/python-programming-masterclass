letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

# create a slice that produces the characters qpo
backwards = letters[16:13:-1]
print(backwards)
# slice the string to produce edcba
backwards = letters[4::-1]
print(backwards)
# Slice the string to produce the last 8 characters in reverse order
backwards = letters[:-9:-1]
print(backwards)

# python idioms
print(letters[::-1])  # reverse the sequence
print(letters[-4:])  # returns the end of the sequence
print(letters[-1:])  # returns the last item in the sequence
print(letters[:1])  # return the first item in the sequence

cars = ["Ford", "Chevy", "Honda"]
print(cars[1][3])

