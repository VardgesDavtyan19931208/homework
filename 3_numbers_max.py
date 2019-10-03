print("Hello, input 3 numbers and I will show the max:")

number_1 = int(input("Input first number: "))
number_2 = int(input("Input second number: "))
number_3 = int(input("Input third number: "))

def maximum(num1,num2,num3):

	if num1 == num2 == num3:
		return "All numbers are equal"
	
	elif num1>=num2 and num1>=num3:
		return  "Max number is " + str(num1)
		
	elif num2>=num1 and num2>=num3:
		return "Max number is " + str(num2)
	
	elif num3>=num1 and num3>=num1:
		return "Max number is " + str(num3)

print(maximum(number_1,number_2,number_3))