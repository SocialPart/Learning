"""Лабораторная работа № 8.  Решение простых дифференциальных и интегральных уравнений используя библиотеку SciPy."""

import scipy.integrate as integrate
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

"""Цель лабораторной работы - научиться решать простые дифференциальные уравнения с помощью модуля интегрирования библиотеки SciPy"""

"""Задачи лабораторной работы: 
1.Научиться производить численное вычисление интегралов заданные различными функциями.. 
2.Освоить принцип решения обычных дифференциальных уравнений с помощью библиотеки SciPy. 
3.Освоить принцип решения системы обычных дифференциальных уравнений с помощью библиотеки SciPy. """

"""Ход работы:"""

"""1.Для работы нам понадобится библиотека SciPy"""

"""2. Рассчитать значение интегралов заданных функций в диапазоне от 0 до 1."""

"""Для этого можно использовать функцию quad() модуля integrate библиотеки SciPy. Функция quad() принимает в качестве аргументов функцию и пределы интеграла. """

result_2 = integrate.quad(lambda x: x**2, 0, 1)
result_4 = integrate.quad(lambda x: x**4, 0, 1)
print(result_2, result_4)

"""2.1. Таким же образом можно посчитать двойной интеграл. Для этой цели можно использовать функцию dblquad()."""

area = integrate.dblquad(lambda x, y: x*y, 0, 1, 0, 1)
print(area)

"""3. С помощью модуля integrate можно решать обычные дифференциальные уравнения. 
3.1. Решить уравнение dy(t)/dt = -ky(t); y(0) = 5 
с помощью функции odeint(). Полученное решение построить в виде графика. Значение k принимает значения от 0.1 до 0.5. """

# функция возвращает dy/dt


def model(y,t,k):
    dydt = -k * y
    return dydt

#Начальные условия
y0 = 5

# временные точки
t = np.linspace(0,20)

#Решение ОДУ
k = 0.1
y1 = odeint(model,y0,t,args=(k,))
k = 0.2
y2 = odeint(model,y0,t,args=(k,))
k = 0.5
y3 = odeint(model,y0,t,args=(k,))

# графики

plt.plot(t,y1,'r-',linewidth=2,label='k=0.1')
plt.plot(t,y2,'b--',linewidth=2,label='k=0.2')
plt.plot(t,y3,'g:',linewidth=2,label='k=0.5')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()

"""3.2. Решить уравнение dy(t)/dt = y(t) + 1 с помощью функции odeint(). Полученное решение построить в виде графика."""


def fun(y,t):
    dydt = y+1
    return dydt

#Начальные условия
y0 = 0

#Задаем временные точки
t = np.linspace(0,20)

#Решаем ДУ

res = odeint(fun, y0, t)

#Строим график

plt.plot(t, res)
plt.show()


"""3.3. Решить систему уравнений dx/dt = 7(e^(-1))t
                                 dy(t)/dt = 3 - y(t)
                                 x(0) = 0
                                 y(0) = 0
с помощью функции odeint(). Полученное решение построить в виде графика. """


# функция возвращает dz/dt
def model(z,t):
    dxdt = 7 * np.exp(-t) * t
    dydt = -z[1] + 3
    dzdt = [dxdt,dydt]
    return dzdt

# начальные услвоия
z0 = [0,0]

# временые точки
t = np.linspace(0,5)

# решение ОДУ
z = odeint(model,z0,t)

# графики
plt.plot(t,z[:,0],'b-',label=r'$\frac{dx}{dt}=3 \; \exp(-t)$')
plt.plot(t,z[:,1],'r--',label=r'$\frac{dy}{dt}=-y+3$')
plt.ylabel('response')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()
