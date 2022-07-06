#Цикл while

current_number =1
while current_number <=5:
	print (current_number)
	current_number +=1

#----------------------
prompt = 'Tell me some thing and i can repeat it back to you'
prompt += '\nEnter "quit" to end the program.'

message = ''
while message != 'quit':
    message = input (prompt)
    if message != 'quit':
        print (message.title())


#-----------------------------------
#Flags

prompt = 'Tell me some thing and i can repeat it back to you'
prompt += '\nEnter "quit" to end the program.'

active = True
while active:
    message = input (prompt)
    if message == 'quit':
        active = False
    else:
        print (message.title())

#-----------------------------------
#break
prompt = 'Tell me some thing and i can repeat it back to you'
prompt += '\nEnter "quit" to end the program.'

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print (message.title())

#-----------------------------------
#continue
current_number = 0

while current_number <10:
    current_number += 1
    if current_number % 2== 0: # если деление без остатка то continue == skip>next
        continue
    print(current_number)


#-----------------------------------
#HW 7.4

prompt = 'Please, choose your toppings'

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f'{topping.title()} add in your order')

#-----------------------------------
#HW 7.5
age = 'How old are you?'

while True:
   tiket_price = input (age)
   if int(tiket_price) < 3:
       print ('Free')
   elif int(tiket_price) >=3 and int(tiket_price) >=12:
       print ('10$')
   else:
       int(tiket_price) > 12
       print('15$')
#-----------------------------------
#HW 7.5
prompt = 'Please, choose your toppings'

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f'{topping.title()} add in your order')
#-----------------------------------
#work with dict in cicle while

unconfirmed_users = ['alice','brian','candace']
confirmed_users=[]

while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

print('\nThe following users have been confurmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#-----------------------------------
#delete from dict in cicle while

pets =['dog','cat','dog','goldfish','cat','rabbit','cat']
print (pets)

while 'cat' in pets:
    pets.remove('cat')

print (pets)

#-----------------------------------
#Fill dict in cicle while

responses = {}

polling_active = True

while polling_active:
    #input name and mountain
    name = input ('f\nWhat is your name?')
    response = input('Which mountain would you like to climb someday?')

    #create dict
    responses[name] = response

    #check for end cicle
    repeat = input ('Would you like to let another person respond? (yes/no)')
    if repeat == 'no':
        polling_active = False

print ('\n----- Roll Result ----')
for name, respond in responses.items():
    print (f'{name.title()} wold like to climb {respond.title()}')

#-----------------------------------
#Exer 7.8
sandwich_orders = ['American sub', 'Bacon', 'Bagel toast',
                  'Baked bean', 'Barbecue', 'Barros Luco','Bauru']

finished_sandwiches = []

while True:
    sandwich_check = sandwich_orders.pop()
    print (f'I made your tuna {sandwich_check}')
    
    finished_sandwiches.append(sandwich_check)

print ('All finished sandwiches')
for fsandwich in finished_sandwiches:
    print(f'\nfsandwich')

#-----------------------------------
#Exer 7.9
sandwich_orders = ['American sub','pastrami', 'Bacon', 'Bagel toast',
                  'Baked bean', 'pastrami', 'Barbecue', 'Barros Luco','Bauru','pastrami']

finished_sandwiches = []

print('Pastrami is ended')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while len(sandwich_orders)>0:
    sandwich_check = sandwich_orders.pop()
    print (f'I made your tuna {sandwich_check}')
    
    finished_sandwiches.append(sandwich_check)

print ('All finished sandwiches')
for fsandwich in finished_sandwiches:
    print(f'{fsandwich}')

#-----------------------------------
#Exer 7.10

prompt_name = 'What is your name?'
prompt_country = 'Which country did your want to go?'

survey_results = {}

while True:
    name = input (prompt_name)
    country = input (prompt_country)
    survey_results[name] = country

    repeat = input ('continue?')
    if repeat == 'no':
        break    

print ('---results---')
for name, country in survey_results.items():
    print (f'{name.title()} whant to go {country.title()}')
