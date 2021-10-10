def fun(n,*args):
	list=[i**n for i in args]
	return list
num=[1,2,3,4,5]
print(fun(3,*num))