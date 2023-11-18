"""Лабораторная работа № 5. Визуализация результатов и данных с помощью библиотеки Matplotlib """

import matplotlib.pyplot as plt
import numpy as np

"""Цель лабораторной работы - приобрести навыки визуализации данных с помощью графиков, используя библиотеку MatPlotLib. 

Задачи лабораторной работы: 
1.Понять основной принцип построения графиков с помощью библиотеки MatPlotLib. 
2.Построить двумерные график. 
Научиться дополнять двумерные графики различными надписями. """

"""1.Построить простой график функции в декартовых координатах с произвольными значениями x и y. 
a.Использовать для этого простую функцию plot. Эта функция является аналогичной функции plot в MatLab. Во первых импортируем библиотеку matplotlib.pyplot """

"""b.Построить график функции:"""

plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()


"""c.Добавим обозначение оси ординат: """

plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.ylabel('some numbers')
plt.show()

"""2.Построить графики функций 
f(x) = x ^ 2
f(x) = x ^ 3
f(x) = x ^ (1/2)
в диапазоне x от 0 до 20 в одних координатных осях. 
a.Использовать для этого простую функцию plot. Эта функция является аналогичной функции plot в MatLab. Во первых импортируем библиотеку matplotlib.pyplot """

x = np.linspace(0, 10, 20)
y1 = x ** 2
y2 = x ** 3
y3 = x ** 0.5
plt.plot(x, y1, 'r--', x, y2, 'bs', x, y3)
plt.show()


"""3.Построить графики с помощью функции figure(). 
a.Построить полотно графика с помощью функции add_subplot()"""

fig = plt.figure()
ax = fig.add_subplot(111)
plt.show()


"""Нанести основные атрибуты на график."""

fig = plt.figure()
ax = fig.add_subplot(111)
fig.set(facecolor = 'grey')
ax.set(facecolor = 'white')
ax.set_xlim([-10, 10])
ax.set_ylim([-2, 2])
ax.set_title('Основы анатомии matplotlib')
ax.set_xlabel('ось абцис (XAxis)')
ax.set_ylabel('ось ординат (YAxis)')
plt.show()

"""c.Создадим несколько графиков на одном Рисунке. """

fig = plt.figure()

ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)

ax_1.set(title = 'ax_1', xticks=[], yticks=[])
ax_2.set(title = 'ax_2', xticks=[], yticks=[])
ax_3.set(title = 'ax_3', xticks=[], yticks=[])
ax_4.set(title = 'ax_4', xticks=[], yticks=[])

plt.show()

"""4.Построить любые графики функций в разных осях на одном рисунке как показано ниже. """

plt.figure()
plt.subplot(221)
plt.plot(x, y1, 'bo', x, y2, 'k')
plt.subplot(222)
plt.plot(x, np.cos(2*np.pi*x), 'r--')
plt.subplot(223)
plt.plot(x, np.cos(2*np.pi*x), 'r--')
plt.subplot(224)
plt.plot(x, np.cos(2*np.pi*x), 'r--')
plt.grid(True)
plt.title('new title')
plt.show()

"""4.4. Построить графики с помощью точек: """

x = np.random.rand(50)
y1 = np.random.rand(50)
y2 = np.random.rand(50)

fig, axes = plt.subplots(2, 2)


axes[0][0].scatter(x, y1, marker = 's', c='fuchsia')
axes[0][0].set_title('marker, c')

colors_1 = np.random.rand(50)
axes[0][1].scatter(x, y1, marker='*', c=colors_1, s=700)
axes[0][1].set_title('marker, c, s')

size = 1000*np.random.rand(50)
axes[1][0].scatter(x, y2, marker='o', c='lightcoral', s=size, linewidths=2, edgecolors='darkred')
axes[1][0].set_title('marker, linewidths, edgecolors, c, s')

size = 1000*np.random.rand(50)
colors_2 = np.random.rand(50)
axes[1][1].scatter(x, y2, marker='o', c=colors_2, s=size, edgecolors='black', alpha=0.6)
axes[1][1].set_title('marker, linewidths, edgecolors, alpha, c, s')

fig.set_figwidth(12)	#  ширина и
fig.set_figheight(12)	#  высота "Figure"
plt.show()
