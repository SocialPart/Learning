"""Лабораторная работа No 6. Использование Python функций
в расчетах инженерных задач."""

import math as ma
import matplotlib.pyplot as plt

"""Цель работы - создавать Python функции и применять их для расчета инженерных задач.

Задачи:

Задача 1. Написать код для решения задачи цепи постоянного тока. Сделать
проверку решения с помощью логических выражений на основе баланса мощностей.

Задача 2. Написать код для решения задачи цепи переменного тока, используя
комплексные значения. Сделать проверку решения с помощью логических
выражений на основе баланса мощностей.

Задача 3. Рассчитать цепь переменного тока, используя мгновенные значения тока и
напряжения с помощью типа переменных массив. Построить основные характеристики.

Именная функция

Функция в python - объект, принимающий аргументы и возвращающий значение.
Обычно функция определяется с помощью инструкции def. Команда return
указывает, что возвращать при вызове этой функции. Python функция может
возвращать любую переменную, объект и даже функцию. Пример простой функции"""

# def myFun(x,y):
#     return x + y
# print(myFun(10, 5))

#Функция не обязательно должна иметь команду return.

# def helloWorldFun():
#     print('hello world')
# fun1 = helloWorldFun()
# print(fun)

"""Тогда переменная fun будет иметь переменную None."""


# def helloWorldFun():
#     print('hello world')
#
#
# fun2 = helloWorldFun()
# print(fun)

"""Аргументы функции"""

"""Функция может принимать произвольное количество аргументов. Стоит отметить,
что есть обязательные аргументы функции и необязательные. Необязательнуые
аргументы функции определяются через оператор присваивания при ее создании."""

# def newFun(a, b, c, d = 5, e = 'test'):
#     print(a, b, c ,d ,e)
#
# print(newFun(1, 4, 3, e = 'other'))

"""Можно передавать произвольное количество неименованных и именованных
аргументов. Для произвольного количества не именованных аргументов
используют обозначение *args, а для именованных **kwargs. Тогда в теле цикла
будут доступные переменные args (это кортеж с переданными данными) и kwargs
(это словарь, где ключ название переменной, а значение словаря это значение
переданной переменной)"""

# def newFun(*args, **kwargs):
#     print(args, kwargs)
#     return args, kwargs
#
# s = newFun(1, 'dva', (32, 33), k = 2, d = 'tri')
# print(s)

"""Написать функцию, которая принимает значений амплитуды, времени и частоты и
выдает расcчитанное значение по формуле 𝑢 = 𝑈𝑚𝑎𝑥𝑐𝑜𝑠(2𝜋𝑓1𝑡). Построить график
этой функции."""


u_max = 220
f1 = 50
def source(u_max, time, freq):
    """Эта функция расчитывает значение напряжения по заданным
    параметрам:
    u_max - амплитуда
    time - текущее вермя,
    freq -частота"""
    return u_max * ma.cos(2 * ma.pi * freq * time)

data = ([source(u_max, t/1000, f1) for t in range(100)] , [t/1000 for t in range(100)])

plt.plot(data[1], data[0])
plt.show()

source.__doc__

'Эта функция рассчитывает значение напряжения по заданным\n параметрам:\n u_max - амплитуда\n time - текущее время,\n freq -частота'

"""
1. Написать функцию для создания последовательности времени как тип
переменной список. На входе эта переменная получает нулевое значение
времени, конечное значение времени и количество точек в этой
последовательности. Эта функция должна выдавать список со значениями
времени.
2. Написать функцию которая выдает список со значениями, рассчитанными по
формуле 𝑢 = 𝑈𝑚𝑎𝑥𝑐𝑜𝑠(2𝜋𝑓1𝑡). Аргументы у этой функции должны быть
амплитуда, список значений времени и частота."""

def CreateTimeList(t_start, t_stop, points = 100):
    time_list = [t_start]
    step = (t_stop - t_start) / points
    for i in range(points):
        time_list.append(time_list[i]+step)
    return time_list

a = CreateTimeList(1,10,100)
print(a)


def source_list(u_max, time_list, freq):
    data = []
    for t in time_list:
        value = u_max * ma.cos(2* ma.pi * freq * t)
        data.append(value)
    return data

time_list = CreateTimeList(0, 0.1, points=100)
data = source_list(u_max, time_list, f1)
print(time_list, data)
plt.plot(time_list, data)
plt.show()


"""Lambda-функции"""

"""Любая функция типа
def myFun(agr1, arg2, argN ...):
    <code>
    return expression
может быть переписана в более компактном виде, используя Lambda-функции.
myFun = lambda arg1, arg2, argN, ...: expression"""

def orderFun(x, order=2):
    return x ** order

orderFun_lambda = lambda x, order: x**order

y1 = []
y2 = []

x_list = range(10)
for x in x_list:
    y1.append(orderFun(x, 2))
    y2.append(orderFun_lambda(x, 2))

plt.plot(x_list, y1, x_list, y2)
plt.show()

def L(x, n):
    s = 0
    for i in range (1, n+1):
        s += (1.0/i)*(x/(1.0+x))**i
    return s

"""Дополнительное задание на лабораторной. Вывести количество сочетаний элементов списка списков"""

def combinations_from_list_of_lists(*args: list) -> list:

    #Расчёт максимального размера результата (количество сочетаний списков)

    args = list(args)
    sum_length = len(args[0])
    for i in range(1, len(args)):
        sum_length *= len(args[i])

    #Расчёт максимального размера результата (количество сочетаний списков)

    if len(args) == 1:
        return args[0]

    #Начало расчёта

    res = []
    for i in range(len(args[0])):
        prom = []
        for j in range(len(args[1])):
            prom.append(args[0][i])
            prom.append(args[1][j])
            res.append(prom)
            prom = []
    args.pop(1)
    args[0] = res

    #Цикл добавляющий в списки первого подсписка элементы следующего подсписка (перебор)
    #Также он присваивает резльтат первому подсписку и удаляет следующий
    #Пока длина первого подсписка меньше суммарной длины

    while len(args[0]) < sum_length:
        prom = []
        for i in range(len(args[0])):
            for j in range(len(args[1])):
                srom = args[0][i].copy()
                srom.append(args[1][j])
                prom.append(srom)
        args[0] = prom
        args.pop(1)

    return args[0]

a = combinations_from_list_of_lists([1, 2, 3], [4, 6, 6, 6])
print()
print(a)