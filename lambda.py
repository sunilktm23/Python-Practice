def num(n):
	return lambda a:a*n;
n=int(input("Enter number ="))
b=num(n)
for i in range(1,11):
	print(n,"X",i,"=",b(i));