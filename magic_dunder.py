class Emp:
	inc=1.5
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
	def incr(self):
		self.salary=self.salary*Emp.inc
	def__add__(self, other):
		return self.salary+other.salary
sunil=Emp("sunil","mahakud",100000)
sanjay=Emp("sanjay","purohit",1000)
print(sunil.fname,sunil.lname,sunil.salary)
sunil.incr()
print(sunil.salary)
print(sunil+sanjay)