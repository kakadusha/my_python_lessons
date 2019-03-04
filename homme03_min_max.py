# ДомашнееЗадание №3
# Написать программу, которая запрашивает у пользователя два числа, а затем выводит максимальное из них. Использовать условные операторы if ... else.
# Усложнённое задание: запросить три числа и вывести минимальное и максимальное из них.


def Min(a1, a2, a3 = None):
	if a3 is None:
		return min (a1, a2) 
	else:
		return min (a1, a2, a3) 
	
def Max (a1, a2, a3 = None):            
	if a3 is None:
		return max (a1, a2) 
	else:
		return max (a1, a2, a3)


n = int(input("Сколько чисел (2 или 3): "))



if n == 3 :
	i1 = int(input("Введите число 1: "))
	i2 = int(input("Введите число 2: "))
	i3 = int(input("Введите число 3: "))        
	print(i1, i2, i3)
	print('Minimum ', Min (i1, i2, i3))
	print('Maximum ', Max (i1, i2, i3))
       
if n == 2 :
	i1 = int(input("Введите число 1: "))
	i2 = int(input("Введите число 2: "))
	i3 = None
	print(i1, i2)
	print('Minimum ', Min (i1, i2, i3))
	print('Maximum ', Max (i1, i2, i3))
                   


 