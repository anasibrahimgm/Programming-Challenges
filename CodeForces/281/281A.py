str = input()

if (len(str) <= 1000):
	list = list(str)

	list[0] = list[0].upper()

	str2 = ''.join(list)

	print(str2)
