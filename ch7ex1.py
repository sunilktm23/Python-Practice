n=int(input("Enter n = "))
def cube(a):
	cub={}
	for i in range(1,a+1):
		cub[i]=i**3
		
	return cub
print(cube(n))