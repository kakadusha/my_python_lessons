#
# #ДомашнееЗадание №12
#  Получить от пользователя строку чисел и занести их в список. 
#  Составить новый список, хранящий все числа из старого, но только без повторений. 
#  Вывести на экран числа из нового списка и количество их повторений в старом.
#                                                        
############################################################################################################
import collections
c = collections.Counter()

s = input("Введите несколько числе через пробел: ")

nums = s.split()
#for i in range(len(nums)):
#	nums[i]=int(nums[i])


for e in nums:
	c[e] += 1
      	
num_sort = nums  
num_sort.sort()
print("Теперь сортированный список: ", num_sort)
print("Counter:                     ", c)
print("Counter.values:              ", c.values())
print("Elements:                    ", list(c))

for i in list(c):
	print('Element ', i,' - ',c[i], ' time(s)') 