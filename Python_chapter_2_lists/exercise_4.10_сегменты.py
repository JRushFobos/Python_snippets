my_foods = ['pizza','falafel','carrot cake','pizza1','falafel1','carrot cake1']
print (my_foods[:3])
print (my_foods[2:-2])
print (my_foods[-2:])
friend_pizzas = my_foods[:]
my_foods.append('tufu')
friend_pizzas.append('kung fu')
print ('My favorite pizzas are:')
for i in my_foods:
	print (i)

print ("\nMy frend's favorite pizzas are:")
for i in friend_pizzas:
	print (i)

menu = ('\n\nпюре','винигрет','колбаса','сыр','омлет')
for i in menu:
	print (i)

#menu.append('pizza')
menu = ('pizza','tea')
for i in menu:
	print (i)