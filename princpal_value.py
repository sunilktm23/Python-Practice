
def value(p,n,period):
	sum=p
	year=1
	while year<=period:
		sum=sum*(1+n)
		year+=1
	return sum
	
a=float(input("Enter princpal value = "))
b=float(input("Enter inrate value = "))
per=int(input("Enter period = "))
ans=value(a,b,per)
print("-"*20)
print("-"*20)
print(str(ans))
print("-"*20)
print("-"*20)

		