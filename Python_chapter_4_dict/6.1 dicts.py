person = {
	'first_name':'Katia',
	'last_name':'Bogacheva',
	'age':'28',
	'city':'Perm',
	}

for i in person.values():
	print (i)
for i in person.keys():
	print (i)

for i,a in person.items():
	print (i,a)


#--------------------
numbers = {
	'Katia':'62',
	'Sasha':'33',
	'Pasha':'63',
	'Lena':'27',
	}

for i in numbers.keys():
	print (f'Любимое число {i} - {numbers[i]}')

#--------------------
#Перебор ключей и значений

user_0={'username':'efemi',
		'first':'emrico',
		'last':'fermi',
		}

for key,value in user_0.items():
	print (f'\nKey:{key}')
	print (f'Value:{value}')


#-----------------------
#Перебор ключей

favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'rudy',
	'phil':'python',
	}

friends = {'phil','sarah'}

for name in favorite_languages:#keys():
	print (f'Hi {name.title()}')

	if name in friends:
		language = favorite_languages[name]
		print (f'{name.title()}, I see y favorite language is {language.title()}')

if 'Vali' not in favorite_languages:
	print ('vali take our poll')

#--------------------------------
#Перебор ключей словаря с сортировкой ключей

for i in sorted(favorite_languages.keys()):
	print (f'Thanks for taking the poll {i.title()}')

#------------------------------

rivers = {'nile':'egipt',
		  'amazonca':'brazil',
		  'volga':'russia',}

for river in rivers.keys():
	print (river)

for country in rivers.values():
	print (country)

#-------------------------
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'rudy',
	'phil':'python',
	}

friends = {'phil','sarah','john','oleg'}
	
for name in friends:
	if name in favorite_languages:
		print (f'Thanks {name.title()}, for learn {favorite_languages[name]}')
	else:
		print (f'{name.title()} do you want learn language?')

#-----------------------
#Словарь в списке, генерация словаря

aliens = []

for aliens_number in range(30):
	new_alien = {'color':'green', 'point':5,'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print (alien)

print ('...')

print(f'Total aliens now is {len(aliens)}')

for alien in aliens[:3]:
	if alien['color']  == 'green':
		alien['color'] = 'red'
		alien['point'] = 3
		alien['speed'] = 'medium' 

for alien in aliens[:5]:
	print (alien)

print ('...')

print(f'Total aliens now is {len(aliens)}')

#----------------------
#Список в словаре

pizza = {
	'chust':'thick',
	'toppings':['mushrooms', 'extra cheese']
	}

print (f"You order is {pizza['chust']}")

for topping in pizza['toppings']:
	print ('\t' + topping)

#-----------------------

favorite_languages = {
	'jen': ['python''ruby'],
	'sarah':['c'],
	'edward':['rudy','go'],
	'phil':['python','haskell'],
	}

for name, languages in favorite_languages.items():
	if len(favorite_languages[name])==1:
		for language in languages:
			print (f"{name.title()}'s favorite language is {language.title()}")
	else:
		print (f'\n{name.title()} favorite languages are:')
		for language in languages:
			print (f'\t {language.title()}')

#--------------------------
#Словарь в словаре

user= {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
		},
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris',
		}
	}

for user_name, user_info in user.items():
	print (f'\nUsername: {user_name.title()}')
	print (f"\tUserInfo: {user_info['first'].title()}, {user_info['last'].title()}")
	print (f"\tUserLocation: {user_info['location'].title()}")