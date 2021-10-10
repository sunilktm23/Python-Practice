fp=open("file.txt","a+")
fp.write("some time")
if fp:
	print("append sucseccful")
c=fp.read()
print(c)

ft=open("file2.txt","r");

ct=ft.read();
print(ct)