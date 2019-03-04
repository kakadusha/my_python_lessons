'''
#ДомашнееЗадание №13
Дан список из целых чисел. 
Поменяйте местами первый минимальный и первый максимальный элемент этого списка.

Решите задачу несколькими способами. Например, с использованием специальных функций и методов, и без них.
'''
####################################################################################
import time

def max_min_my(nums_list):
	'''
	Считает вручную минимум и максимум
	'''
	m_max = nums_list[0] # максимальный элемент
	m_min = nums_list[0] # минимальный элемент
	for m in nums:
		m_max = m if m_max < m else m_max
		m_min = m if m_min > m else m_min
	return(m_max, m_min)



s = input("Введите несколько числе через пробел: ")

nums = s.split()
for i in range(len(nums)):
	nums[i] = int(nums[i])

print('Ваш список: ',nums)

start_time = time.process_time()

m_max,m_min = max_min_my(nums)

print('Время выполнения ', time.process_time() - start_time, "seconds")
print('Max: ', m_max)
print('Min: ', m_min)

print('------')

start_time = time.process_time()
m_min_auto,m_max_auto = min(nums),max(nums)
print('Время выполнения ', time.process_time() - start_time, "seconds")
print('Max_auto: ', m_max_auto)
print('Min_auto: ', m_min_auto)

print('-----------------------------------------------------------------------')
print('--давайте нормально развлечемся, создадим большую последовательность ')
N = int(input('Сколько случайных чисел возьмем? '))
print('Делаю...');
import random        
random.seed()
nums=[]
for i in range(N):
	nums.append(random.randint(0, N))
print('У нас ', len(nums), 'чисел');

start_time = time.process_time()

m_max,m_min = max_min_my(nums)

print('Время выполнения ', time.process_time() - start_time, "seconds")
print('Max: ', m_max)
print('Min: ', m_min)

print('------')

start_time = time.process_time()
m_min_auto,m_max_auto = min(nums),max(nums)
print('Время выполнения ', time.process_time() - start_time, "seconds")
print('Max_auto: ', m_max_auto)
print('Min_auto: ', m_min_auto)

print('-- Ну как? Автометод быстрее? или вы победили?')
