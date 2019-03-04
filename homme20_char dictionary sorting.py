#ДомашнееЗадание №20
'''
Статистический анализатор

На вход программы поступает текстовая строка. Создать структуру данных типа словарь, 
в которой в качестве ключа выступает символ из текста, а в качестве значения - 
количество таких символов в тексте. 

Вывести на экран построчно в порядке убывания вероятности следующую информацию: 
символ, количество, вероятность встречи такого символа в исходном тексте в процентах.

1) https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html 
2) https://younglinux.info/python/dictionary.php
3) https://tproger.ru/explain/python-dictionaries/
^^ Словари в Питоне

'''
S = input('Введите строку для статистического анализа : ')

d = {}

for c in S:
	#print(c, d[c])
	d[c] = d.setdefault(c, 0) + 1

# print(d.keys())
for c, n in d.items():
    print('Имеем символ {0} счетчик {1}'.format(c, n))

#Чтобы использовать значения
s_v = sorted(d.values())
print( 'Сортированные значения: ', format(s_v) )
#Чтобы получить соответствующие клавиши, используйте функцию key
s_k = sorted(d, key=d.get)
print( 'Сортированные ключи   : ', format(s_k) )
print( 'Сортированные пары: ' )
for k in s_k: print ( '[', k, '] = ', d[k] )

print('А теперь через лямбда функцию! Cписок кортежей, упорядоченных по значению :')
print ( sorted(d.items(), key=lambda x:-x[1]) )