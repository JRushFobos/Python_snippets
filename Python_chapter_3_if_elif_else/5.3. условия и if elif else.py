alian_color = 'red'
if alian_color == 'green':
	print ('Игрок заработал 5 очков')
elif alian_color== 'red':
	print ('Игрок заработал 10 очков')
else:
	print ('Игрок заработал 10 очков')


age = 25
if age < 2:
	print ('Младенец')
elif age >= 2 and age <4:
	print ('Малыш')
elif age >=4 and age <13:
	print ('Ребенок')
elif age >= 13 and age < 20:
	print ('Подросток')
elif age >=20 and age < 65:
	print ('Взрослый')
elif age >65:
	print ('Пожилой')

available_toppings = ['mushrooms','olives','green pepers', 'peperoni','pineapple','extra cheese']

requested_toppings = ['mush_rooms','fench fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print (f'Adding {requested_topping}.')
else:
	print (f'Sorry we not have {requested_topping}.')
print ('Finished making your pizza') 


users = ['admin','Luna','Dasha','Sasha','kira']
if users:
	for user in users:
		if user == 'admin':
			print (f'Hello {user}, would you like to see a status report?')
		else:
			print (f'Hello {user}, thank you fo logging in again')



current_users = ['admin','Luna','Dasha','SASHa','kira']

current_users=[element.lower() for element in current_users]

new_users = ['admin','LUNA','katia','Sasha','tolia']

for user in new_users:
	if user.lower() in current_users:
		print (f'Пользователь {user} уже зарегистрирован, выбери другое имя пользователя')
	else:
		print (f'Можно зарегистрироваться с именем {user}')

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
	if number == 1:
		print (f'{number}st')
	elif number == 2:
		print (f'{number}nd')
	else:
		print (f'{number}th')