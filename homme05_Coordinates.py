#
#     NOT READY
#	                   

n1 = input("Введите имя 1: ")
n2 = input("Введите имя 2: ")
n3 = input("Введите имя 3: ")
print(n1, n2, n3)

if (n1 <= n2) and (n1 <= n3): 
	print('a 1: ', n1)
	if n2 <= n3: 		
		print('aa2: ', n2)
		print('aa3: ', n3)
	else:            
		print('ab2: ', n3)
		print('ab3: ', n2)


if (n2 < n1) and (n2 <= n3): 
	print('b 1: ', n2)
	if n1 <= n3: 		
		print('ba2: ', n1)
		print('ba3: ', n3)
	else:            
		print('bb2: ', n3)
		print('bb3: ', n1)
 


if (n3 < n1) and (n3 < n2): 
	print('c 1: ', n3)
	if n1 <= n2: 		
		print('ca2: ', n1)
		print('ca3: ', n2)
	else:            
		print('cb2: ', n2)
		print('cb3: ', n1)
 