class Emp:
	inc=1.5
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
	def incr(self):
		self.salary=self.salary*Emp.inc
	@classmethod
	def change(cls,amount):
		 inc=amount
sunil=Emp("sunil","mahakud",100000)
sanjay=Emp("sanjay","purohit",1000)
print(sunil.fname,sunil.lname,sunil.salary)
sunil.incr()
print(sunil.salary)
Emp.change(3)
sunil.incr()
print(sunil.salary)
