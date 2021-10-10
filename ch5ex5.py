num1=[1,2,3,4]
num2=[1,2,5,6]
def clist(a,b):
	out=[]
	for i in a:
		if i in b:
			out.append(i)
		
	return out
print(clist(num1,num2))
		
		