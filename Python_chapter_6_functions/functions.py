#functions

def greet_user(username):
	'''comment'''
	print (username.title())

greet_user('jesse')

#---------------------------------
#Exer 8.1

def display_message():
	print ('Learn functions')

display_message()

#---------------------------------
#Exer 8.2

def favorite_book (book_name):
	print (f'One of my favorite books is {book_name}')

favorite_book('Alice on Wonderland')

#---------------------------------
#Позиционный аргументы в параметрах функции

def describe_pet(animal_type, pet_name):
	'''information'''
	print(f'\nI have a {animal_type}')
	print(f"\nMy {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster','harry')

#---------------------------------
#Именнованные аргументы в парметрах функции

def describe_pet(animal_type, pet_name):
	'''information'''
	print(f'\nI have a {animal_type}')
	print(f"\nMy {animal_type}'s name is {pet_name.title()}")

describe_pet(animal_type='hamster',pet_name='harry')

#---------------------------------
#Аргументы поумолчанию
def describe_pet(pet_name, animal_type='dog'): #порядок важен
	'''information'''
	print(f'\nI have a {animal_type}')
	print(f"\nMy {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='harry')

#---------------------------------
#Exer 8.3

def make_shirt(size,shirt_print):
	print(f'Shirt have a size {size} and print {shirt_print}')

make_shirt('XL','Python the TOP')
make_shirt(size='XXXL',shirt_print='Hello World')

#---------------------------------
#Exer 8.4

def make_shirt(size='L',shirt_print='I love Python'):
	print(f'Shirt have a size {size} and print {shirt_print}')

make_shirt(60,'Python the TOP')
make_shirt(size=54,shirt_print='Hello World')
make_shirt()

#---------------------------------
#Exer 8.5

def describe_city(city, country='Russia'): 

	print(f"\n{city.title()} is in {country.title()}")

describe_city('Perm')
describe_city('London','UK')
describe_city('Rim','Italy')

#---------------------------------
#Return

def get_formatted_name(first_name, last_name):
	full_name = f'{first_name} {last_name}'
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print (musician)

#---------------------------------
#Optional attribute

def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = f'{first_name} {middle_name} {last_name}'
	else:
		full_name = f'{first_name} {last_name}'
	return full_name.title()

musician = get_formatted_name('john','hooker','lee')
print (musician)

musician = get_formatted_name('jimi','hendrix')
print (musician)

#---------------------------------
#Functions and dict

def build_person(first_name, last_name, age=None): #empty age in if = false
	#Создание списка
	person = {'first':first_name, 'last':first_name}
	if age:
		person['age']=age
	return person

musician = build_person('jimi','hendrix',age=27)
print(musician)

#---------------------------------
#Functions with interruption

def get_formatted_name(first_name, last_name):
	full_name = f'{first_name} {last_name}'
	return full_name.title()

while True: 
	print ('Input your name and surname')
	print('Input "q" for quit')
	
	f_name = input('Input your name')
	if f_name == 'q':
		break

	f_surname = input('Input your surname')
	if f_surname == 'q':
		break


	formated_name = get_formatted_name(f_name,f_surname)
	print (formated_name)

#---------------------------------
#Exer 8.6

def city_country(city,country):
	travel = f'{city.title()} {country.title()}'
	return travel

while True:
	fcity = input('Input City')
	if fcity =='q':
		break
	fcountry = input('Input country')
	if fcountry == 'q':
		break
	ftravel = city_country(fcity,fcountry)
	print (ftravel)

#---------------------------------
#Exer 8.7

def make_album(atrist,album,track=None):
	if track:
		result = {'atrist': atrist, 'album': album, 'track':track}
	else:
		result = {'atrist': atrist, 'album': album}
	return result

prodigy = make_album('The Prodigy', 'Omen')
stromae = make_album('Stromae','Alors on Danse')
isaak = make_album('Chris Isaak',' Wicked Game')
sean = make_album('Jay Sean','Ride it',track=10)

print (prodigy)
print (stromae)
print (isaak)
print (sean)

#---------------------------------
#Exer 8.8
def make_album(artist,album,track=None)
	result = {'artist':artist, 'album': album}
	if track:
		result['track']=track
	return result

print('Input Artist, Album and count tracks*')
while = True:
	f_artist = input ('Input Artist name')
	if f_artist == 'q'
		break

	f_album = input('Input Album title')
	if f_album == 'q'
		break
	f_track = input ('Input count tracks')
	if f_track == 'q'
		break

	out = make_album(f_artist,f_album,f_track=None)
	print(out)

#---------------------------------
#Exer 8.9

def make_album(artist,album,track=None):
	result = {'artist':artist, 'album': album}
	if track:
		result['track']=track
	return result

print('Input Artist, Album title and count tracks*')
while True:
	f_artist = input ('Input Artist name')
	if f_artist == 'q':
		break

	f_album = input('Input Album title')
	if f_album == 'q':
		break

	f_track = input ('Input count tracks')
	if f_track == None:
		f_track = None
	elif f_track == 'q':
		break

	out = make_album(f_artist,f_album,f_track)
	if 'track' in out:
		print (f"Artist: {out['artist']}, Album title: {out['album']},Tracks: {out['track']}")
	else:
		print (f"Artist: {out['artist']}, Album title: {out['album']}")

#---------------------------------
#Functions with list
#Send list in function

def greet_user(names):
	for name in names:
		msg= f'Hello, {name.title()}'
		print (msg)

usernames = ['hannah','ty','margot']
greet_user(usernames)

#---------------------------------
#Functions with list
#Change list in function

unprintind_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

while unprintind_designs:
	current_designs = unprintind_designs.pop()
	print(current_designs)
	completed_models.append(current_designs)

print ('\nThe following models have been printed:')
for compleated_model in completed_models:
	print (completed_model.title())
#---------------------------------
#OR with 2 functions
def print_models (unprinted_designs,compleated_models):

	while unprintind_designs:
	current_designs = unprintind_designs.pop()
	print(current_designs)
	completed_models.append(current_designs)

def show_compleated_models(completed_models):
	for compleated_model in completed_models:
		print (completed_model.title())

unprintind_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models (unprinted_designs,compleated_models)
show_compleated_models(completed_models)