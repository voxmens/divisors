import sys

divisors = []

def isDivisible(num1, num2):
	if(num1%num2 == 0):
		return True
	return False

num = int(sys.argv[1])

for i in range(1, num+1):
	if(isDivisible(num, i)):
		divisors.append(i)

print(divisors)
