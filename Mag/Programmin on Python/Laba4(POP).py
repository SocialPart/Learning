"""Лабораторная работа № 4. Численное решение систем уравнений с помощью библиотеки NumPy. """

import numpy as np

"""Цель лабораторной работы - освоить основные подходы линейной алгебры для решения систем линейных уравнений с помощью библиотеки NumPy. 

Задачи лабораторной работы: 
1.Научиться находить обратную матриц. 
2.Научиться представлять систему уравнений в матричном виде. 
3.Решать системы уравнений с помощью разных методов. """

"""Ход работы:"""

"""1.Решить систему уравнений различными методами, используя библиотеку NumPy
x + 2y = 1
3x + 5y = 2
"""

"""1.1.Импортируем библиотеку в код программы:"""

"""1.2.Представим систему уравнений в матричном виде. Левая часть уравнения записывается в виде матрицы, а правая в виде вектор-столбца. """

a = np.array([[1, 2], [3, 5]])
b = np.array([7, 8])

"""1.3.Решить систему методом Крамера. Определитель матрицы найти с помощью функции np.linalg.det(). Для этого сделаем копии двухмерных массивов 
(матриц) с помощью метода copy(). В одной из матриц заменим первый столбец на свободные члены, во второй матрице заменим второй столбец на свободные матрицы. 
Выведем основную матрицу и замененную на экран. """

a1 = a.copy()
a2 = a.copy()
a1[:, 0] = b
a2[:, 1] = b
print(a)
print(a1)
print(a2)

"""1.4 Найдем определители каждой из получившихся матриц. А искомые значения найдем из деления вспомогательных определителей на основной"""

det = np.linalg.det(a)
det1 = np.linalg.det(a1)
det2 = np.linalg.det(a2)

x1 = det1/det
x2 = det2/det

print('x=', x1, 'y=', x2)

"""1.5.Проверить решение с помощью функции allclose(). Эта функция сравнивает две матрицы и выводит логическую переменную True или False 
в зависимости от совпадения или не совпадения массивов. 
Для этих целей напишем собисвенную функцию, которая выдает корректное или некорректное решение системы уравнений. """


def checkSol(x, a, b):
    if np.allclose(np.dot(a, x), b) == True:
        print('Я решил правильно!')
    else:
        print('Я решил неправильно')


x = [x1, x2]
checkSol(x, a, b)

"""1.6.Решим с помощью встроенной функции linalg.solve. Эта функция позволяет выдавать численное решение системы уравнений
на основе основной матрицы уравнений и свободных членов. """

x = np.linalg.solve(a,b)

"""2.Решить систему уравнений с помощью обратной матрицы"""

"""X = (A^(-1)) * B"""

x = np.dot(np.linalg.inv(a), b)
print(x)

"""2.1.Проверить решение с помощью написанной функции для проверки уравнений. """

checkSol(x, a, b)

"""2.2.Другая запись решения системы уравнений может быть записана следующим образом"""

x = np.linalg.inv(a).dot(b)


"""3.Решить систему уравнений со свободными членами используя любой метод"""
"""5x1 -3x2 + 10 = 3
   23x3 - 25x2 + 31x1 + 7 = 6
   3/9x1 + 2/3x2 = 31"""

"""3.1.Для этого преобразуем уравнение к матричному виду и запишем его с помощью следующего кода:"""

a = np.array([[5, -3, 0], [31, -25, 23], [3/9, 2/3, 0]])
b = np.array([-7, -1, 31])
x = np.linalg.solve(a, b)
print(x)

checkSol(x, a, b)
