number = int(input("Hello, input number: "))

def fizz_buzz(num):
	if num % 3 == 0 and num % 5 != 0:
		return "Fizz"
	elif num % 5 == 0 and num % 3 != 0:
		return "Buzz"
	elif num % 3 == 0 and num % 5 == 0:
		return "FizzBuzz"
	else:
		return num

print(fizz_buzz(number))