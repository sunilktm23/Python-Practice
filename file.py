fileptr=open("file.txt","r")
if fileptr:
	print("File isopened")
content=fileptr.read()
c=fileptr.readline();
print(content)
print(c)