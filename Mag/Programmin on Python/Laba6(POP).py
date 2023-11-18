"""Лабораторная работа № 6.  Решение уравнение и задач оптимизации с использоание библиотеки SciPy."""

import numpy as np
import scipy as sp
from numpy import pi, r_
import matplotlib.pyplot as plt
from scipy import optimize
from scipy import special
from scipy.optimize import curve_fit

"""Цель лабораторной работы - приобрести навыки визуализации данных с помощью графиков, используя библиотеку MatPlotLib. 

Задачи лабораторной работы: 
1.Научиться строить простые графики. 
2.Научиться представлять систему уравнений в матричном виде. 
3.Решать системы уравнений с помощью разных методов. """

"""Ход работы:"""

"""1. Импортируем библиотеки:"""
"""Найдем минимум функции y(x) = x ^ 2 . """
"""2.1. Для начала построим график этой функции."""

x = np.arange(-10, 10, 0.01)
y = x ** 2
plt.plot(x, y)
plt.show()

"""2.2. Создадим Python-функцию для функции  с помощью lambda оператора. Используя функцию fminbound() в модуле optimize 
библиотеки SciPy найдем наименьшее значение этой функции в пределах от -10 до 10. Выведем минимальное значение на экран."""

f = lambda x: x**2
lim_min = -10
lim_max = 10

x_min = optimize.fminbound(f, lim_min, lim_max)
plt.plot(x, y)
plt.plot(x_min, f(x_min),'bo')
plt.show()

"""2.3. Повторим подобное для функций Бесселя в диапазоне от 0 до 10 и членов Бесселя от 0.5 до 5.5.  """

x = np.arange(0,10,0.01)

for k in np.arange(0.5,5.5):
    y = special.jv(k,x)
    plt.plot(x,y)
    f = lambda x: -special.jv(k,x)
    x_max = optimize.fminbound(f,0,6)
    plt.plot([x_max], [special.jv(k,x_max)],'ro')

plt.title('Different Bessel functions and their local maxima')
plt.show()

"""3.1. Подбор функции по заданным значения. Создадим функцию . Добавим искажения с помощью случайной 
функции шума согласно нормальному распределению Гаусса. Построим эти функции на графике."""

freq = 50
omega = 2 * np.pi * freq
T = 1/freq
phi0 = 0
x = np.arange(0, 10*T, T/40)

fun = lambda x: np.sin(omega*x+phi0)*x
noise = lambda x: np.sin(x)*x*np.random.normal(size=fun(x).size)
final_fun = lambda x: fun(x) + noise(x)
plt.plot(x, final_fun(x), 'ro')
plt.plot(x, fun(x))
plt.show()

"""3.2. Используя методы оптимизации подберем коэффициенты для a и b для функции , чтобы она подходила к зашумленной функции.  
Это можно реализовать с помощью следующего кода: """



def test(x, a, b):
    return b*np.sin(omega*x)*x**a

param, param_cov = curve_fit(test, x, final_fun(x))

print("Sine function coefficients:")
print(param)
print("Covariance of coefficients:")
print(param_cov)
ans = test(x, param[0], param[1])

plt.plot(x, final_fun(x), 'o', color='red', label="data")
plt.plot(x, ans, '--', color='black', label="optimized data")
plt.plot(x, fun(x), label='real function')
plt.legend()
plt.show()