############problem
# Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.
# What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

###########idea
#cover the Square with k*l flagstones of size a^2 such that ka >= n && la >= m

import math

n, m, a = input().split();
#inputString = input()
#inputList = inputString.split(' ')
# n = int(inputList[0])

n = int(n)
m = int(m)
a = int(a)

if not(n >= 1 and m >= 1 and a >=1 and a <= math.pow(10, 9)):
	print("Wrong Input Values!")
	
else:
	#number of flagstones = ceil(n/a) * ceil(m/a)
	num = math.ceil(n/a) * math.ceil(m/a)

	print(num)