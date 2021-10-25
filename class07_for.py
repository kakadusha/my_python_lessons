# 

for x in [1,2,3,'abb']:
	print (x) 
print('----')

#for x in 'abbgrtdgsojty':
#	print (x) 
#print('----')

list(range(1,10))
print('--list 1 10--')

list(range(1,10,2))
print('--list 1 10 2--')

for x in range(0,10):
	print(x)
print('--1-10--')

sum_ = 0
for x in range(1,101):
	#print(x)
	sum_+=x

print('sum: ',sum_)

print( sum(list(range(1,101))) )
	