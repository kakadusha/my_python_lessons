#!/usr/bin/env python
# coding: utf-8

# #  Вложенные функции, замыкания и декораторы

# ## 1. Функции

# **Функция** — часть программы, которую можно вызвать из другого места программы.
# 
# Все в Python объекты. И даже функции. Это значит, что у функций есть
# - атрибуты
# - и методы.
# 
# От остальных объектов функции отличаются тем, что их можно вызвать*. Объекты, которые можно вызвать, называют `Callable`-объектами. У них есть метод `__call__()`.
# 
# \* С точки зрения синтаксиса еще можно вызывать классы

# ### Как определить функцию

# In[2]:


# Функция определяется таким синтаксисом
def plus_one(x: int) -> int:
    """Функция возвращает увеличенное на 1 целое число"""
    return x+1


# Это избыточное определение. Из избыточного здесь использованы:
# - строка документирования — `docstring`,
# - и анотация функции.
# 
# На самом деле можно описать эту же функцию компактней. 

# In[3]:


# Функция plus_one без анотаций и документации
def plus_one_simple(x): return x+1


# ### Функция как объект

# Как у любого объекта в python, у функции есть:
# - идентификатор,
# - тип.

# In[4]:


# У функции plus_one эти параметры выглядят так
print(id(plus_one), type(plus_one))


# В CPython идентификатор — **адрес объекта** в виртуальной памяти

# In[5]:


# Идентификатор в шестнадцатиричном формате — адрес функции plus_one
print(hex(id(plus_one)))


# Все атрибуты и методы функции как объекта можно посмотреть:

# In[6]:


import inspect
#for l in list(filter(lambda x: x[0] != "__globals__", sorted(inspect.getmembers(plus_one)))): print(l) 
# Здесь мы выбросили поле "__globals__", чтобы не засорять вывод


# ### Как вызвать функцию

# In[7]:


#  Вызов функции, ожидаем ответ 2
plus_one(1)


# In[8]:


#  Можно явно вызвать метод call, ожидаем ответ 2
plus_one.__call__(1)


# ### Как функции устроены

# In[9]:


# Байт-код функции function_name
print(plus_one.__code__.co_code)


# In[10]:


# Дизассемблированное тело функции function_name
import dis
dis.dis(plus_one)

import sys
sys.exit()
# Если заглянуть во внутренности интерпретатора (CPython), то функция описывается следующей струтурой: https://github.com/python/cpython/blob/3.7/Include/funcobject.h

# ### Почитать
# 1. [The Python Language Reference. Data model](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
# 2. [The Python Language Reference. Inspect live objects](https://docs.python.org/3/library/inspect.html)
# 3. [PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/)
# 4. [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

# ## 2. Вложенные функции

# **Вложенная функция** — функция, которая определена внутри другой функции.
# 
# При работе с вложенными функциями надо учитывать области видимости.

# ### Область видимости в Python — LEGB

# В Python есть 4 области видимости. Расположены они как показано на рисунке.
# 
# ![title](img/LEGB.png)
# 
# Стрелки на рисунке показывают в какой последовательности Python обходит области видимости. Следующий код показывает как распределены области относительно вложенной функции inner.

# In[10]:


# (built-in) — область системных имен

# global — область модуля
def outer():
    # enclosed — область функции-обёртки 
    def inner():
        # local — область внутри функции
        pass


# ### Зачем нужны вложенные функции?

# Зачем это может быть нужно? Можно выделить 3 примера:
# 1. чтобы скрыть функцию в глобальной области видимости,
# 2. чтобы вынести «лишний» код из функцию в обёртку,
# 3. чтобы реализовать замыкания (см. следующий раздел).

# #### Пример 1. Чтобы скрыть функцию — инкапсуляция

# In[11]:


# Вложенная функция inner внутри plus_one_outer
def plus_one_outer(x):
    """Функция возвращает увеличенное на 1 целое число"""
    def inner(y): return y+1
    return inner(x)
    


# In[12]:


#  Вызов функции, ожидаем ответ 2
plus_one_outer(1)


# In[13]:


# Вложенная функция недоступна (должна быть ошибка)
inner(1)


# Вложенные функции дают накладные расходы

# In[ ]:


import dis
dis.dis(plus_one_outer)


# #### Пример 2. Чтобы вынести «лишний» код из функции в обёртку

# In[ ]:


def factorial(x):
    """Функция вычисляет факториал целого числа"""
    def calc_factorial(y): return y * calc_factorial(y-1) if y!=0 else 1
    if x<0:
        return -1
    return calc_factorial(x)
    


# In[ ]:


factorial(4)


# ## 3. Замыкания

# **Замыкание** — вложенная функция, которая запоминает значения окружения, с которым она была вызвана. Говорят, что функция «замыкается» на значения переменных окружения. По сути это техника параметризированной генерации функций.
# 
# Рассмотрим простой пример замыкания

# In[ ]:


# Функция-обёртка принимает возвращает внутренную функцию, которая «замкнута» на значение a
def gen_mul(a):
    def inner(b):
        return a*b
    return inner


# In[ ]:


# gen_mul возвращает функцию, которая будет всегда умножать на 2
double = gen_mul(2)


# In[ ]:


# Проверим (должно быть 6)
double(3)


# In[ ]:


# Можно возвращаемую функцию не сохранять
gen_mul(2)(3)


# Функции, которые возвращают другие функции, называются **«фабриками функций»**.

# ## 4. Декораторы

# **Декоратор** — «синтаксический сахар» для функции-обёртки вокруг другой функции. Обычно декоратор используют, чтобы добавить новое поведение другой функции без изменения ее тела.

# In[ ]:


# Возьмем простую функцию возведения в квадрат
def sqr(x): return x*x
sqr(5)


# ### Пример элементарного декоратора

# Мы хотим обёрнуть функцию возведения в квадрат другой функцией, чтобы добавить новые возможности.
# Ниже приведен пример фабрики функций, которая возвращает функцию-обёртку. Эта функция-обёртка выполняет новый код
# и вызывает оборачивемую функцию.

# In[ ]:


from time import perf_counter_ns

# Фабрика функций, которая генерирует обернутые функции func для отладки вызова и результата
def make_debugable(func):
    def wrapper(x):
        print(f"[DEBUG] Launch function {func} with x={x}")
        start_time_ns = perf_counter_ns()
        result = func(x)
        stop_time_ns = perf_counter_ns()
        duration_ns = stop_time_ns-start_time_ns
        print(f"[DEBUG] Time: {duration_ns}ns")
        return result
    return wrapper


# Обернём функцию sqr, сгенерированное значение будем хранить в sqrt2.

# In[ ]:


sqrt2 = make_debugable(sqr)
sqrt2(5)


# Синтаксический сахар декораторов позволяет описать такое поведение короче. При этом декоратор генерирует обёрнутую функцию с таким же именем как у обораичиваемой.

# In[ ]:


# Следующий код эквивалентен: sqr3 = make_debugable(sqr3)
@make_debugable
def sqr3(x): return x*x

sqr3(4)


# #### Практичный пример применения декоратора `make_debugable`

# Сравним скорость работы встроенной функции `sum` с написанной «руками» с помощью декоратора `make_debugable`.

# In[ ]:


@make_debugable
def sum_1(n):
    """Суммирование числе от 1 до n в цикле for"""
    s = 0
    for i in range(n):
        s += i
    return s


# In[ ]:


@make_debugable
def sum_2(n):
    """Суммирование числе от 1 до n встроенной функцией"""
    return sum(range(n))


# In[ ]:


sum_1(10000)


# In[ ]:


sum_2(10000)


# Наглядно видно, что встроенная функция производительней.

# ### Пример рабочего декоратора

# По сути декоратор возвращает другую функцию. Если проверить документацию к функции:

# In[ ]:


# Проверка справки (не должен вернуть строку)
help(sum_1)


# Чтобы возвращаемая функция была похожа на оборачиваемую надо скопировать внутреннии атрибуты.

# In[ ]:


from functools import wraps
from time import perf_counter_ns

# Улучшенная фабрика функций, которая генерирует обернутые функции func для отладки вызова и результата
def make_debugable_real(func):
    @wraps(func) # Декоратор из библиотеки для копирования внутренних атрибутов
    def wrapper(x):
        print(f"[DEBUG] Launch function {func} with x={x}")
        start_time_ns = perf_counter_ns()
        result = func(x)
        stop_time_ns = perf_counter_ns()
        duration_ns = stop_time_ns-start_time_ns
        print(f"[DEBUG] Time: {duration_ns}ns")
        return result
    return wrapper


# In[ ]:


@make_debugable_real
def sum_3(n):
    """Суммирование числе от 1 до n встроенной функцией"""
    return sum(range(n))


# In[ ]:


# Проверка справки (теперь должен вернуть строку)
help(sum_3)


# ### Пример рабочего декоратора с параметрами

# Чтобы декоратор принимал аргументы, надо сформировать замыкание фабрики обёрток с параметром декоратора.

# In[ ]:


from functools import wraps

# Фабрика генераторов функций, которая позволяет использовать параметры, функция умножает результат функции на число.
def mul(p):
    def decorator(func):
        @wraps(func)
        def wrapper(*args): # Упаковали параметры (см. ниже)
            return p*func(*args) # Распаковали параметры обратно (см. ниже)
        return wrapper
    return decorator


# Объявим функцию с двумя декораторами. Декораторы применяются последовательнос снизу вверх.

# In[ ]:


@mul(2)
@mul(4)
def f(x: int, y: int):
    return x+y


# In[ ]:


# Должно быть 24 так как 2(4(1+2)) = 24
f(1,2)


# #### Упаковка и распаковка параметров

# При работе с последовательностями можно собирать значения в переменные. Это называется **упаковка**. Синтаксис такой.

# In[ ]:


a, *b, c = [2, 7, 5, 6, 3, 4, 1]


# В `b` теперь список всего того, что не попало в `a` и `c`

# In[ ]:


print(b)


# Эти значения можно подставить используя **распаковку**.

# In[ ]:


print(*b)


# Результат вывода разный. В первом случае вызов эквивалентен `print([b1, b2, b3])`, во втором — `print(b1, b2, b3)`.
# 
# **NB!** Упаковка и распоковка доступна и для словарей. Для этого используется **.