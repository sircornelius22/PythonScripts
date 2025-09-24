for x in range (1, 101):
	num = ""
	if x%3 == 0 and x%5 == 0:
		num += "FizzBuzz"
	elif x%3 == 0:
		num += "Fizz"
	elif x%5 == 0:
		num += "Buzz"
	if num == "":
		print(x)
	else:
		print(num)
