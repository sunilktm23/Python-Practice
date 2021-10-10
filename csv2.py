import csv
with open('Python.csv','w')as f:
	fieldnames=['fname','lname','rank']
	writer=csv.DictWriter(f,fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'rank':'A','fname':'Parker','lname':'Brian'})
	writer.writerow({'rank':'B','fname':'Sunil','lname':'Mahakud'})
	writer.writerow({'rank':'C','fname':'Sanjay','lname':'Singh'})
print("Writing complete")