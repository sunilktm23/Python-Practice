def cubes(n):
	c={ }
	for i in range(1,n+1):
		c[i]=i**3
	return c
print(cubes(3))