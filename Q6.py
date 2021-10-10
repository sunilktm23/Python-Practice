import math
c=50
h=30
value=[]
i=[x for x in input("Enter = ").split(',')]
for d in i:
	value.append(str(int(math.sqrt(2*c*float(d)/h))))
print(','.join(value))