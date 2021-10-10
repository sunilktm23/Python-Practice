n=int(input("Enter n = "))
for i in range(1,n+1):
	for s in range(1,40-(i*2)):
		print(" ", end="")
	for j in range(1,i+1):
		print(i, end="")
	print("\n")
for k in range(i-2,0):
	for s in range(1,40-(i*2)):
		print(" ", end="")
	for j in range(1,i+1):
		print(i, end="")
	k=k-1
	print("\n")