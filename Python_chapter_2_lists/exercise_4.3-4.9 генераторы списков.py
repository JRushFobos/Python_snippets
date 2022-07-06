for i in range (1,21):
	print (i)


list_1_1_000_000 = [value for value in range(1,1_000_001)]
print (min (list_1_1_000_000))
print (max (list_1_1_000_000))
print (sum (list_1_1_000_000))
#for i in list_1_1_000_000:
	#print(i)

#нечетные
for i in range (1,21+1,2):
	print (i)

#кратные 3
list_1 = [value for value in range(3,31) if value %3 == 0]
for i in list_1:
	print (i)

list_1 = [value **3 for value in range(1,11) ]
kube=[]
for i in list_1:
	kube.append(i)

print(kube)	