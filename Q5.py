class inout():
	def __init__(self):
		self.s=""
	def getstr(self):
		self.s=input("Enter string= ")
	def printstr(self):
		print(self.s)
a=inout()
a.getstr()
a.printstr()