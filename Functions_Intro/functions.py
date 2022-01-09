def multiply(x: float, y: float) -> float:
    """
    Multiply two values together.

    The function will receive two numbers and multiply them together.

    :param x: First value to use
    :param y: Second value to use
    :return: The result of multiplying `x` by `y`
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    # backwards = string[::-1]
    # return backwards == string  # returns true or false
    return string[::-1].casefold() == string.casefold()  # more concise version


# My solution
def palindrome_sentence(string: str) -> bool:
    """
    Check if sentence is a palindrome.

    This function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param string: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    new_string = ''
    for char in string:
        if char.isalnum():
            new_string += char
    print(new_string)
    return is_palindrome(new_string)


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, for positive n."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result


for i in range(36):
    print(i, fibonacci(i))

# answer = multiply(18, 3)
# print(answer)

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

