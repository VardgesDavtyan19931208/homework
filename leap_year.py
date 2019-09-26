year = input("Hello, please enter the year: ")

a = int(year)%4
b = int(year)%100
c = int(year)%400

if a != 0:
	print("not leap")
elif a == 0 and b != 0:
	print("leap")
elif a == 0 and b == 0 and c != 0:
	print("not leap")
elif a == 0 and b == 0 and c == 0:
	print("leap")

print("(c) gregorian calendar ")
