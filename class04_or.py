# Функция для нахождения среднего 3х чисел
def Median(i1, i2=None, i3=None, i4=None):
	return ( (i1 + i2 + i3)/3 )

print( Median ( 
	int(input("Введите число 1: ")), 
	int(input("Введите число 2: ")), 
	int(input("Введите число 3: ")) 
	) )
                                                                                

