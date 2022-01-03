# panagram = """The quick brown
# fox jumps\tover
# the lazy dog"""
# words = panagram.split()
# print(words)
#
# numbers = "9, 223, 372, 036, 854, 775, 807"
# print(numbers.split(","))


#  Mini challenge
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)
values_list = values.split()
print("values list: {}".format(values_list))

#  replace in list
# for i in range(len(values_list)):
#     values_list[i] = int(values_list[i])
# print(values_list)


#  create new list
int_values = []

# my version
# for i in range(len(values_list)):
#     int_values.append(int(values_list[i]))

# Tim's version
for value in values_list:
    int_values.append(int(value))
print(int_values)


