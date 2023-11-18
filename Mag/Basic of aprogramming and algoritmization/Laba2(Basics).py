# Лабораторная работа 2. Работа с основными типами переменных Python

"""Задача 1. Ознакомиться с основными типами данных (переменных) и понять
принцип их классификации

Задача 2. Приобрести первичные навыки реализации переменных чисел (int,
float, complex) и изучить основные функции для манипуляций над этими
переменными

Задача 3. Усвоить назначение типа переменной строка (str) и понять
принципы работы с данной переменой. Изучить основные операции над
строкой

Задача 4. Изучить назначение переменных типа список. Произвести ряд
встроенных операций над ними и сделать выводы о различии кортежа и
списка

Задача 5. Понять назначение переменных типа словарь и изучить основные
операции над ним"""

"""Типы данных в Python можно разделить на 
1. None - неопределенное
значение 
2. Логические переменны (Boolean Type) 
3. Числа 1. int - целое
число 2. float - число с плавающей точкой 3. complex - комплексное число
4. Списки 1. list - список 2. tuple - кортеж 3. range - диапазон 
5. Строки str - запись текста 
6. Словари dict И ряд других, например бинарные списки (bytes, bytearray, memoryview),
множества (set, frozenset), но это не входит в изучение нашего курса.

Проверка типа переменной можно осуществить с помощью функции
type(имя_переменной)

Стоит выделить также что переменные в Python могут быть изменяемыми и
неизменяемыми. Это обозначает, что созданная переменная не может
измениться после ее создания. 

Неизменяемые переменные: целые числа (int),числа с плавающей точкой (float), 
комплексные числа (complex), логические переменные (bool), кортежи (tuple), 
строки (str) и неизменяемые множества (frozen set). 
Изменяемые переменные: списки (list), множества (set), словари (dict)."""

"""Работа с целыми, дробными и комплексными числами"""

"""Целое число в Python имеет тип int (integer). Под целыми числами понимаются положительных, 
отрицательных множество чисел и ноль не имеющие дробную часть. По-умолчанию любое цело число 
инициализируется как тип int."""

a = 5
print(type(a))

"""Числа с плавающей точкой или другими словами вещественные числа.
Инициализация данной переменой можно осуществить следующим образом"""

a = 1.0
print('a is ', type(a))
b = 23.3333
print('b is ', type(b))
c = float(5)
print('c is ', type(c))

"""Важным в математических и инженерных расчетах являются комплексные числа.
Их инициализация производится с помощью функции complex(real part, image part) 
или использование символа мнимой единицы 1j"""

z1 = complex(1, 2)
print('value of z1 is',z1,'type is',type(z1))
z2 = 1 + 1j * 2
print('value of z2 is',z2,'type is',type(z2))


"""Основные операции над переменными чисел

Если у переменной с типом float поменять тип на int, тогда число будет
округлено в сторону нуля. Если переменную float конвертировать в тип
complex, тогда мнимая часть будет равна нулю."""

d = 15.78
print(int(d))
print(complex(d))

"""Функции для типа int
abs(int_number) - вывести модуль целого числа.

Функции для типа float
abs(float_number) - вывести модуль вещественного числа.
Функция round(float_number) - округляет число в меньшую сторону.

Функции для типа complex
abs(float_number) - вывести модуль комплексного числа.
float_number.imag - вывести реальную часть
float_number.real - вывести мнимую часть
float_number.conjugate - вывести сопряженное число"""

int_number = -15
print('Модуль числа', abs(int_number))

float_number = -15.0
print(type(round(float_number)), round(float_number))
print("Модуль вещественного числа", abs(float_number))

complex_number = complex(-15, -15)
print(complex_number)
print(complex_number.imag)
print(complex_number.real)
print(complex_number.conjugate())
print('Модуль комплексного числа', abs(complex_number))


#Произвести простые операции с числами

d1 = 15
d2 = 2
result = d1/d2
print('It\'s result', result, 'with type', type(result))

result += complex(1, 1)
print('It\'s result', result, 'with type', type(result))

result_real = result.real
result_imag = result.imag
result_conjugate = result.conjugate()
print('It is real part', result_real, 'with type', type(result_real))
print('It is image part', result_imag, 'with type', type(result_imag))
print('It is conjugate', result_conjugate, 'with type', type(result_conjugate))

#Работа со строками. Тип str.

"""Тип строки переменной в Python подразумевает под собой текстовые данные. 
Один из самых популярных программ в Python - это вывод строки Hello world."""


print('Hello world')

"""Инициализация переменной типа str осуществляется с помощью двух паострофов или кавычек. Между этими методами разницы нет."""

test_text1 = 'Hello world'
print(test_text1)
test_text2 = "Hello world"
print(test_text2)

"""Основные функции доступные для обработки переменных строки

Оператор + присоединяет одну строку к другой
Оператор * дублирует строку n раз.
Функция len(string) - возвращает количество символов в строке"""

string1 = 'hello'
string2 = 'bye bye'

print(string1+string2)
print(string1*3)
print(len(string1))

"""Интересной функцией является вывод символов по порядковому номеру. Для этого после названия переменной в квадратных скобках необходимо указать номер символа. 
Символ : указывает, что вывести все символы."""

print(string1[:]+string2[3:])

"""Часто всречаются многострочные тексты. Для реализации такой переменной с текстом в Python необходимо использовать экранированные операторы.
•первеод на новую строку
•горизонтальная табуляция
•вертикальная табуляция
Удобно также использовать тройные кавычки или апострафы для рабоыт смногострочным текстом."""

string3 = '\t Hello world \n and buy world, \n \t but we are here'
print(string3)

string4 = '''Hello world 
we are here but 
we are goin to leave'''
print(string4)


"""Работа со списками 

Списки в Python (list) - упорядоченные изменяемые коллекции
объектов произвольных типов (почти как массив, но типы могут отличаться).
Создать переменную списка можно с помощью квадратных скобок или функции list()."""

new_list = [1, 2, 3, 'heello', 23*1j]
print(new_list, type(new_list))

new_list_2 = list('hello wolrd')
print(new_list_2)

"""Основыне функции работы со списками

list.append(x) - добавить элемент x в конец списка list

list.extend(L) - расширить list списком L

list.insert(i, x) - вставить x на i место в списке list

list.remove(x) - удалить первый элемент со значением x в списке list

list.pop([i]) - удалить i элемент

list.reverse() - сделать обратную последовательность списка

list.clear() - удалить список"""

my_list = [1, 2, 3, 4]
my_list_new = [3, 4, 5, 10]
i = 5

my_list.append(my_list_new)
print(my_list)

my_list.extend(my_list_new)
print(my_list)

my_list.insert(i, my_list_new)
print(my_list)

my_list.remove(my_list_new)
print(my_list)

my_list.pop(i)
print(my_list)

my_list.reverse()
print(my_list)

my_list.clear()
print(my_list)

"""Доступ к элементам списка"""

"""Доступ к элементам списка осуществляется с помощью порядкого номера, который указывается в квадратных скобках после переменной списка. 
Доступ по индексу list[10]. Можно вывести сразу выборку от i до j элемента list[i:j]. Стоит отметить, что элемент с номером j не входит в срез. 
Нумерация производится с нулевого номера элемента. В языке Python доступны отрицательные номера индексов, 
это означает обратную индексацию или другими словами отсчет с конца списка."""

new_list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(new_list_4[0])
print(new_list_4[-1])
print(new_list_4[2:3])
print(new_list_4[2:7])
print(new_list_4[0:-1:2])
print(new_list_4[0:-1:3])

"""Элементы списка можно изменять обращаясь к ним по индексам и используя оператор присваивания."""

new_list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(new_list_4)
new_list_4[0] = 'I am new here'
print(new_list_4)
new_list_4[-1] = 'I am new here'
print(new_list_4)

"""Операции над списками"""

list_1 = [1, 2, 3]
list_2 = [3, 4, 5]
k = 2
print(list_1 * k)
print(k*list_1)
print(list_1 + list_2)

"""Кортежи (tuple) в Python – это те же списки за одним исключением. Кортежи неизменяемые структуры данных. 
Так же как списки они могут состоять из элементов разных типов, перечисленных через запятую. 
Кортежи заключаются в круглые, а не квадратные скобки. Также можно их инициализировать с помощью функции tuple()"""

my_tuple = ()
print('Это мой пустой кортедж ', my_tuple, "тип корджа обозначается так", type(my_tuple))

my_tuple_new = ('hello world', 1, 3, 4, [123])
print('Это мой пустой кортедж ', my_tuple_new, "тип корджа обозначается так", type(my_tuple_new))

"""Можно извлекать элементы из кортежа и брать срезы как со списками"""

print(my_tuple_new[2])
print(my_tuple_new[2:5])

"""Но мы не можем заменять элементы в кортеже"""

my_tuple_new[2] = 3 #Выведет ошибку

"""Тип переменной словарь"""

"""Тип переменной словарь часто используется в программах Python. Python словарь - это упорядоченый набор данных доступ к которым производится с помощью ключа. 
Словарь является подобием списко, только доступ к ним осуществляется не по индексу,а по произвольному ключу. 
Ключем может быть любой неизменяемый тип данных Python. Значит кортеж может быть ключем, а списки нет."""

my_empty_dictionary = {}
my_dictionary_1 = {'myName': 'Alexander', 'myLastName': 'Efimov'}

print(my_dictionary_1)

my_dictionary_2 = dict(myName='Alexander', myLastName='Efimov')
print(my_dictionary_2)
my_dictionary_3 = dict.fromkeys(['myName', 'myLastName'], 'Alexnder Efimov')
print(my_dictionary_3)

"""Вывод значений словаря"""

new_dict = {'numbers': [1,2,3,4], 'characters': ['a', 'b', 'c'], 'float_values': [25.3, 34.6, 37.2]}

print(new_dict['numbers'])
print(new_dict['characters'])
print(new_dict['float_values'])

"""Можно заменить значение словаря обращаясь к нему по ключу и используя знак присваивание."""

new_dict['numbers'] = 'new numbers'
new_dict['characters'] = 'here change something'
print(new_dict)

"""Основные функции работы со словарем
dict.values() - выводит значения в словаре
dict.keys() - выводит список всех ключей словаря
dict.items - возвращает пару ключ и значение
dict.pop(key) - удаляет ключ и возращает значение.
dict.get(key) - возвращает значение по ключу, если нет такого ключа возвращает тип None."""

our_new_dict = {'students': ['Vasya, Petya', 'Sasha'], 'Marks': [3, 4, 5], 1: ['test1, test2, test3'], (1,2,3): 'test tuple'}
print('It is our values of dictionary', our_new_dict.values())
print('It is our keys of dictionary', our_new_dict.keys())
print('It is ourvalues of dictionary', our_new_dict.values())

