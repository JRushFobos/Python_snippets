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