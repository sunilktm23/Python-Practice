user={'name':'harshit','age':23}
print(user)
user1=dict(name='Sunil',age=18)
print(user1)
print(user1['name'])
for key,values in user1.items(): 
	print(f"keys is {key} and values is {values}")
print(user.pop('name'))
print(user.popitem())