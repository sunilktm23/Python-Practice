
def summi(a):
	if a==0:
		return 1
	return a*summi(a-1)
n=int(input("Enter your numbeer = "))

print((summi(n)))