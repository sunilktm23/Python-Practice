dims=[int(x) for x in input("Enter = ").split(",") ]
rawD=dims[0]
colD=dims[1]
list=[[0 for col in range(colD)] for raw in range(rawD)]
for raw in range(rawD):
	for col in range(colD):
		list[raw][col]=raw*col
print(list)