people = [
	{
	'first_name':'Katia',
	'last_name':'Bogacheva',
	'age':'28',
	'city':'Perm',
	},
	{
	'first_name':'pasha',
	'last_name':'sidorov',
	'age':'40',
	'city':'mosсow',
	},
	{
	'first_name':'dmitry',
	'last_name':'pevcov',
	'age':'60',
	'city':'osa',
	},
	]

for i in people:

	print (f'\nName {i["first_name"].title()}')
	print (f'Surname {i["last_name"].title()}')
	print (f'Age {i["age"].title()}')
	print (f'City {i["city"].title()}')

#------------------------------------------

pets = [
	{'name':'dina',
	'type':'cat',
	'owner':'john'},
	 {'name':'uma',
	'type':'dog',
	'owner':'pasha'},
	 {'name':'mickey',
	'type':'mouse',
	'owner':'lena'},
	]

for pet in pets:
	print (f'\nName pet is {pet["name"].title()}')
	print (f'Type pet is {pet["type"].title()}')
	print (f'Owner pet"s is {pet["owner"].title()}')

#-------------------------
favorite_places = {
    'sam':['nowyork','london','paris'],
    'jack':['beijing','tokyo'],
    'rose':['ottawa'],
    }

for name,cites in favorite_places.items():
	print (f'Name {name.title()} lives in:')
	for city in cites:
		print (f'\t{city.title()}')

#----------------------------


favorite_nums = {'jack':[8,16,32],
                 'lucy':[5,10,15],
                 'ben':[14],
                 'joe':[19,20,40],
                 'kate':[21],
                 }

for name, numb in favorite_nums.items():
	print (f'{name.title()} have favorite number:')
	for num in numb:
		print (f'{num}')

#-----------------------

cities = {
    'guangzhou':{
        'country':'china',
        'population':'700w',
        'fact':'canton',
        },
    'london':{
        'country':'United Kingdom',
        'population':'800w',
        'fact':'modern',
        },
    'newyork':{
        'country':'United States',
        'population':'850w',
        'fact':'modern',
        }
        }
for city, city_info in cities.items():
	print (f'City: {city.title()}')
	print (f'\t{city_info["country"]}')
	print (f'\t{city_info["population"]}')
	print (f'\t{city_info["fact"]}')  