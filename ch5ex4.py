num=list(range(1,11))
def slist(l):
	o=[]
	e=[]
	for i in l:
		if i%2==0:
			o.append(i)
		else:
			e.append(i)
			
	output=[o,e]
	return  output
print(slist(num))