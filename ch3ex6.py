win=43
num=int(input("Enter any num between 1 to 100 = "))
guess=1
game_over=False
while not game_over:
	if num== win:
		print(f"You win, you tried {guess} times")
		game_over=True
	else:
		if num > win:
			print("too high")
		elif num < win:
			print("too low")
		guess += 1
		num=int(input("Enter again = "))
	
    