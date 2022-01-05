def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string  # returns true or false
    return string[::-1].casefold() == string.casefold()  # more concise version


# My solution
def palindrome_sentence(string):
    new_string = ''
    for char in string:
        if char.isalnum():
            new_string += char
    print(new_string)
    return is_palindrome(new_string)


answer = multiply(18, 3)
print(answer)

# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print()
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)
#


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# sentence = input("Please enter a sentence to check: ")
# if palindrome_sentence(sentence):
#     print("'{}' is a palindrome".format(sentence))
# else:
#     print("'{}' is not a palindrome".format(sentence))
