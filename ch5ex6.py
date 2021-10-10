from typing import List, Union

num: List[Union[int, List[int]]]=[1,2,[2,3],[3,4]]
def nlist(a):
	count=0
	for i in a:
		if type(i)==list:
			count+=1
	return count
print(nlist(num))