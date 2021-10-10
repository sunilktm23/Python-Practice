def fibonacci(num):
	a=0
	b=1
	if num==1:
		print(a)
	elif num==2:
		print(a, b)
	else:
		print(a,b, end=" ")
		for i in range(n-2):
			c=a+b
			a=b
			b=c
			print(b, end=" ")
			
			
n=int(input("Enter number = "))
print(fibonacci(n))
			