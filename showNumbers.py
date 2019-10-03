limit = int(input("Input the limit: "))

range_by_user = range(0,limit)

for i in range_by_user:
	if i % 2 == 0:
		print(i, " EVEN")
	elif i % 2 != 0:
		print(i, " ODD")