def paramodia(name):
	a=name
	b=name[ : :-1]
	if a==b:
		print("name is paramodia ")
	else:
		print("NOT A PARAMODIA")
a=input("Enter a name = ")
print(paramodia(a))
