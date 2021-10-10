a=int(input('Enter n ='))
def patern(n):
	for i in range(0,n+1):
		for s in range(1,40-(i*2)+1):
			print(" ")
		for j in range(1,i+1):
			print("*   ")
			
print(patern(a))