"""Лабораторная работа № 7.  Символьное вычисление уравнений с использованием библиотеки SimPy."""

import sympy as sym
import math as ma

"""Цель лабораторной работы - научиться работать с библиотекой символьного вычисления SymPy"""

"""Задачи лабораторной работы: 
1.Научиться записывать выражения в символьном виде. 
2.Освоить основные подходы составления символьных выражений. 
3.Производить вычисления основных математических операций в символьном виде. """


"""Часть примеров перед лабой"""

# sym.pprint(sym.Integral(x**2))
#
# ser = sym.limit(sym.cos(x),x, -sym.oo)
# sym.pprint(ser)

"""Посчитаем производную функции"""

# res = sym.diff(x**4, x)
# sym.pprint(res)

"""Символьное ввычисление"""
# y = sym.symbols('y')
# sym.pprint(sym.solve(y**2 - 2, y))

"""Дифференциальные уравнения"""

# y = sym.Function('y')
# t = sym.symbols('t')
# equation = sym.Eq(y(t).diff(t,t) - y(t), sym.exp(t))
# result = sym.dsolve(equation, y(t))
# sym.pprint(result)

"""Ход работы:

1.Для работы нам понадобиться библиотека sympy и math"""

"""2.Сравнить вычисление с помощью библиотеки math и символьного вычисления.
2.1. Выведем на экран число 2^(1/2) с помощью библиотеки math и sumpy"""

print(ma.sqrt(2), sym.sqrt(2))
sym.pprint(sym.sqrt(2))

"""2.2. Выведем на экран число  с помощью библиотеки math и sumpy"""

print(ma.sqrt(12), sym.sqrt(12))
sym.pprint(sym.sqrt(12))

"""2.3. Представить выражение в виде символов. В виде символа будет выступать x. Для этого запишем следующий код:"""

x = sym.Symbol ('x')
sym.pprint(x)

"""2.4. Запишем выражение , где a=5 и выведем на экран получившееся выражение с помощью команд 
print()и sym.print()."""

a = 5
sym.sqrt(a)
sym.pprint(sym.sqrt(a))
print(sym.sqrt(a))

"""2.5. Запишем в символьном виде выражение интеграла"""

sym.pprint(sym.Integral(x**x, x))

"""Запишем в символьном выражении формулу √√e^x"""

sym.pprint(sym.sqrt(sym.sqrt(sym.exp(x))))

"""2.6. Удобно иногда использовать метод series(x, n_0, n),
чтобы разложить в ряд символьную функцию.
Реализуем эту возможность для функции 1/cos, чтобы разложить в многочлены от 0 степени до 10 порядка."""

sym.pprint((1/sym.cos(x)).series(x, 0, 10))

"""3. Работа с символами. 
3.1. Можно присваивать переменным Python символьное значение 
и затем использовать эту переменную в символьных выражениях или 
для составления этого символьного выражения.

Создадим переменную x1 и x2 как x_1и x_2 с помощью функции 
sym.Symbol(). Затем создадим функцию 
$y = (x_1+x_2 )^2 $ и выведем ее на экран.
"""
x1 = sym.symbols('x1')
x2 = sym.symbols('x2')
y = (x1+x2)**2
sym.pprint(y)


"""4. Разложить на множители. Созданное символьное выражение можно 
раскладывать на множители с помощью метода expand() """

sym.pprint(y.expand())

"""5. Посчитаем производные с использованием символьного вычисления
 С помощью символьного вычисления удобно вычислять производные функций. 
 Посчитаем производные функций
f(x) = x^2
f(x) = x^3
f(x) =1+x^3+e^x
Можно это реализовать с помощью функции sym.diff(f(x), x))
"""

x, y = sym.symbols('x y')
function1 = x**2
function2 = x**3
function3 = 1+ x**3 + sym.exp(x)
sym.pprint(sym.diff(function1, x))
sym.pprint(sym.diff(function2, x))
sym.pprint(sym.diff(function3, x))

"""Посчитаем производную функции от двух переменных"""

function_x_y = x**2*y+y**(2*x)
sym.pprint(sym.diff(sym.diff(function_x_y, x), y))

"""Также можно использовать цепочку вызовов метода diff, 
поочередно для нахождения производных каждой переменной"""

"""6. Посчитаем пределы от функции f(x) стремящейся 
к значению x_0 (lim)┬(x→x_0 ) f(x) на языке Python 
с использованием выражений символьного вычисления 
это запишется как sym.limit(f(x), x, x0). 
Посчитаем предел (lim)┬(x→0) 1/sin(x)
"""

sym.pprint(sym.limit(1/sym.sin(x), x, 0))
expr = 1/sym.sin(x)
expr.limit(x, 0)

sym.pprint(sym.limit(1/sym.sin(x), x, sym.oo))

"""Далее в лабе все есть, нужно решить задания на доске"""

"""1 Задание"""
# y = sym.Function('y')
# x = sym.symbols('x')
# equation = sym.Eq(y(x).diff(x) + y(x).diff(x,x) + y(x) - sym.exp(x), 0)
# result = sym.dsolve(equation, y(x))
# sym.pprint(result)

"""2 Задание"""
#
# x = sym.symbols('x')
# y = sym.symbols('y')
#
# equation = sym.Eq((x**3 + x**2 + 3*x - 10),0)
# sym.pprint(sym.solveset(equation))

"""3 Задание"""

# sym.pprint(sym.limit(sym.exp(x),x,-sym.oo))
#
# y = sym.Function('y')
# t = sym.symbols('t')
# equation = sym.Eq(y(t).diff(t,t) - y(t), sym.exp(t))
# result = sym.dsolve(equation, y(t))
# sym.pprint(result)

"""4 Задание"""

# x = sym.symbols('x')
# y = sym.symbols('y')
# z = sym.symbols('z')
#
# fun_x_y_z = 32*x+3*y+10*y-5*z
# sym.pprint(sym.diff(fun_x_y_z, x))

"""5 Задание"""

var1 = sym.symbols('x')
var2 = sym.symbols('y')
var3 = sym.symbols('z')
exprXYZ = 5*var1+10*var2-27*var3
exprX = sym.diff(-exprXYZ,var1)
exprY = sym.diff(25*exprXYZ, var2)
exprZ = sym.diff(exprXYZ, var3)

sym.pprint(sym.pprint(exprX + exprY + exprZ))

