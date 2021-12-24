number = input("Please enter a series of number, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
# print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))


# initial example
# number = "9,223;372:036 854,775;807"
# separators = ""
#
# for char in number:
#     if not char.isnumeric():
#         separators = separators + char
# print(separators)
#
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])