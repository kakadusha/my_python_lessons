﻿'''
#ДомашнееЗадание №14
Даны три списка целых чисел.

Получить новый список, состоящий из элементов, встречающихся во всех трёх списках. 

Отсортировать новый список по количеству таких элементов во всех трёх списках. То есть от наиболее
часто встречающегося до самого редкого.

При решении воспользуйтесь советами по решению задач в программировании. Например, прохождением 
вручную по различным наборам данных, написанием псевдокода алгоритма программы и другими.
'''
# чстота определяется по суммарному объединенному списку
# элемент должен быть во всех трех списках
######################################

#A = [1,2,3,4,5,8]
#B = [1,2,2,2,8,4,5,0]
#C = [1,1,2,3,4,0,6]
A = [8, 11, 0, 0, 0, 8]
B = [8, 11, 11, 0, 8]
C = [8, 0, 11, 11, 11, 11, 8]


print('Список А ', A)
print('Список B ', B)
print('Список C ', C)

All_set = set(A) & set(B) & set(C)

print('Пересечение множеств ', All_set)

All_list = A+B+C

import collections
c = collections.Counter()
for e in All_list:
	if e in All_set:
		c[e] += 1
 
print("Counter:              ", c)
print("Counter:              ", c.items())

sorted_by_value = sorted(c.items(), reverse = True, key=lambda kv: kv[1])

print("Sorted:              ", sorted_by_value)
print("List in order:       ", end=' ')

for x in sorted_by_value:
	print(x[0],end=' ')
