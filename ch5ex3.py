num=['abc','def','ghi']
def rlist(l):
	a=[]
	for i in range(1,len(num)):
		a=l[i]
		b=a[::-1]
	return b
print(rlist(num))	
	
		