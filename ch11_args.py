def add_num(*args):
	t=0
	for i in args:
		t += i
	return t
print(add_num(1,2,3,4,5,6))