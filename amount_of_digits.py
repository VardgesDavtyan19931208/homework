number_by_user = input("Please insert humber: ")

amount = 0

for i in number_by_user:
	if i != 0:
		amount += 1

print(amount)