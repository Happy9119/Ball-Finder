from random import shuffle
ex = ['', '', 'O', '']
#print(ex)
def s_list(ex):
	shuffle(ex)
	return ex
x = s_list(ex)
#print(x)
def user_guess():
	y = int(input("Enter a guess position of Ball\n"))
	while (y > 4 or y == 0):
		print("Incorect guess option\n Enter again:\n")
		y = int(input("Enter a guess position of Ball\n"))
	return y
y = user_guess()
#print(y)
def game_on(x, y):
	y-=1
	if (x[y] == 'O'):
		print("Guess is Correct")
	else:
		print('Guess is incorrect')
		lol = 0
		for temp in x:
			lol+=1
			if temp =='O':
				print(f'Correct Location is {lol}')		
game_on(x,y)