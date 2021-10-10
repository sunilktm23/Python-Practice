import csv
with open('python.txt') as cf:
	cr=csv.reader=csv.reader(cf,delimiter=',')
	lc=0
	for row in cr:
		if lc==0:
			print(f'column name are {",".join(row)}')
			lc+=1
		else:
			print(f'{row[0]} works in the {row[1]} department, and was born in {row[2]}')
			lc+=1
	print(f'Processed {lc} lines')