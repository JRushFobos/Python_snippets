names = ['Igor','Pasha','Kolia','Dima']
name1 = names[0]
name2 = names[1]
name3 = names[2]
name_pop = names.pop()
print (f'Welcome {name1.upper()}')
print (f'Welcome {name2.upper()}')
print (f'Welcome {name3.upper()}')
print (f'Goodbay {name_pop.upper()}')
names.append('Alex')
name4 = names[3]
print (f'Welcome {name4.upper()}')
print ('New guests: Masha, Dasha, Olia')
names.insert(0,'Masha')
names.insert(2,'Dasha')
names.append('Olia')
name1 = names[0]
name2 = names[1]
name3 = names[2]
name4 = names[3]
name5 = names[4]
name6 = names[5]
name7 = names[6]
print (f'Welcome {name1.upper()}')
print (f'Welcome {name2.upper()}')
print (f'Welcome {name3.upper()}')
print (f'Welcome {name4.upper()}')
print (f'Welcome {name5.upper()}')
print (f'Welcome {name6.upper()}')
print (f'Welcome {name7.upper()}')
names_pop1 = names.pop()
print (f'Sorry {names_pop1} dont come')
names_pop2 = names.pop()
print (f'Sorry {names_pop2} dont come')
names_pop3 = names.pop()
print (f'Sorry {names_pop3} dont come')
names_pop4 = names.pop()
print (f'Sorry {names_pop4} dont come')
names_pop5 = names.pop()
print (f'Sorry {names_pop5} dont come')
print (f'Guest {name1} and {name2} can to come')
del names [1]
del names [0]
names.append('Женя')
print (names)
