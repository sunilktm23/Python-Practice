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
	@staticmethod
	def emp(day):
		if day=="sunday":
			return False
		else:
			return True

sunil=Emp("sunil","mahakud",100000)
sanjay=Emp("sanjay","purohit",1000)
print(sunil.emp("sunday"))
