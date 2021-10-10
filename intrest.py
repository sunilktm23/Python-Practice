a=int(input("1 for simple and 2 for compound = "))
if a==1:
	p=int(input("princple = "))
	i=int(input("intrest = "))
	y=int(input("year = "))
	n=(p*i*y/100)+p
	print(f"Total amount is {n} ")
if a==2:
	p=int(input("princple = "))
	i=int(input("intrest = "))
	y=int(input("year = "))
	n=p*((1+(i/100))**y)
	print(f"Total amount is {n}")
	