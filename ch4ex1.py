def comper(n1,n2):
	if n1>n2:
		print(f"{n1} is greater than {n2}")
	elif n2>n1:
		print(f"{n2} is greater than {n1}")
a=int(input("Enter a number = "))
b=int(input("Enter a number = "))
print(comper(a,b))