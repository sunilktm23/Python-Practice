user={}
name=input("What is your name = ")
age=input("What is your age")
fav_movies=input("What is your fav movies = ").split(",")

user['name']=name
user['age']=age
user['fav_movies']=fav_movies

for keys,values in user.items():
	print(f"{keys}={values}")