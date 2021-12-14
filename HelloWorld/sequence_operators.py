string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"
print(string1 + string2 + string3 + string4 + string5)

print("he's " "probably " "pining " "for the " "fjords")  # plus sign isn't needed for string literal concatenation

print("Hello " * 5)  # repeats the sequence

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

# check if one string is a subset of another
today = "friday"
print("day" in today)       # should be true
print("fri" in today)       # true
print("thur" in today)      # false
print("parrot" in "fjord")  # false







