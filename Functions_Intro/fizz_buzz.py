# Write a function that returns the next answer, in the game of fizz bizz
def fizz_buzz(num: int) -> str:
	"""
	Play fizz buzz.
	:param num: Number to test against 3 and 5.
	:return: Return `fizz` if the number is divisible by 3.
		Return `buzz` is the number is divisible by 5.
		Return `fizz buzz` if the number is divisible by 3 and 5.
		Return the number, converted to string if not divisible by
		3 and 5.
	"""
	# if the number id divisible by both 3 and 5, you say "fizz buzz"
	if (num % 3 == 0) and (num % 5 == 0):
		return "fizz buzz"
	# if the number is divisible by 3, you say "fizz"
	if num % 3 == 0:
		return "fizz"
	# if the number is divisible by 5, you say buzz
	if num % 5 == 0:
		return "buzz"
	return str(num)


# for i in range(1, 101):
# 	value = fizz_buzz(i)
# 	print("{}".format(value))
input("Play Fizz Buzz.  Press ENTER to start")
print()
next_number = 0
while next_number < 99:
	next_number += 1
	print(fizz_buzz(next_number))
	next_number += 1
	correct_answer = fizz_buzz(next_number)
	players_answer = input("Your go: ")
	if players_answer != correct_answer:
		print("You lose, the correct answer was {}".format(correct_answer))
		break
else:
	print("Well done, you reached {}".format(next_number))


