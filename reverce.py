num=list(range(1,11))
def rlist(a):
	r=[]
	for i in a:
		r.append(i)
		a=r[::-1]
	return a
print(rlist(num))