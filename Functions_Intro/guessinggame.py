import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))

# Use while loop to allow for multiple guesses
while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        print("Thanks for playing!")
        break
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than answer
        print("Please guess lower")
else:
    print("Well done, you guessed it")

#  Challenge: rewrite program to check for correct answer first
# if guess == answer:
#     print("You got it the first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#        print("Sorry, you have not guessed correctly")

#  Code before randomizing the answer.
# answer = 5
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
# #  Challenge: rewrite program to check for correct answer first
# if guess == answer:
#     print("You got it the first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")


#  Before Challenge
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it the first time")

#  Initial version
# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it!!!")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")
