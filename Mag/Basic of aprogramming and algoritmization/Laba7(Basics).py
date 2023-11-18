"""Лабораторная работа № 7. Практическое применение Python классов в расчетах инженерных задач."""
import math as ma
import matplotlib.pyplot as plt

"""Цель работы - ознакомиться с основами работы с классами Python.
Задачи:
Задача 1. Ознакомиться с основами синтасиса создания класса Python.
Задача 2. Усвоить основные составляющие класса Python.
Задача 3. Написать класс, который принимает значений амплитуды, времени и частоты и выдает расчитанное значение по формуле и строит этот график этой функции."""

"""1. Создать класс с возможностью строить график синусоиды"""

"""1.1. Создать класс с названием MathFunPlotter.
В этом классе задать необходимые атрибуты частоты и амплитуды функции с помощью конструкции __init__"""


class MathFunPlotter:
    """The class is built to plot mathematic functions"""

    def __init__(self, f1, U):
        """Here you define some attributes of the class as default"""
        self.f1 = f1
        self.u_max = U

    def calculate(self, time):
        u = self.u_max * ma.cos((2 * ma.pi * self.f1) * time)
        return u

    def set_data(self, times):
        self.data = ([self.calculate((t / 100) / self.f1) for t in range(times)], [(t / 100) / self.f1 for t in range(times)])
        print(self.data)
        return self.data

    def plotGraph(self):
        plt.plot(self.data[1], self.data[0], '--')
        plt.show()

"""1.2. Вызвать созданный класс со значениями частоты 50 и амплитуды 220."""

plotter1 = MathFunPlotter(50, 220)

"""1.3. Вывести атрибуты частоты и амплитуды на экран из созданного класса."""

print(plotter1.f1)
print(plotter1.u_max)

"""1.4. Вывести описание класса.
Описание класса можно вывести с помощью команды __doc__. Описанием класса является строки заключенные в тройные кавычки."""

print(plotter1.__doc__)

"""2. Добавить в этот класс возможность вычислять значения в определенный момент времени по формуле u = u_max * cos(2*pi* f1* t)"""

"""2.1 Проверить работоспособность созданного метода"""
plotter2 = MathFunPlotter(50, 220).calculate(0.0333)
print(plotter2)

"""3. Добавить опцию расчета набора данных согласно функции u = u_max * cos(2*pi* f1* t) для ее построения"""

"""3.1. Проверить этот метод для 100 точек времени"""
"""Нужно в методе calculate уменьшить T в несколько раз, для большей дискретизации, а то все время показывает 220"""
plotter3 = MathFunPlotter(50, 220).set_data(1000)
print(plotter3)

"""4. Добавить в класс возможность выводить график этого выражения"""

"""4.1. Построить график  с помощью класса"""

plotter4 = MathFunPlotter(50, 220)
plotter4.set_data(100)
plotter4.plotGraph()

"""5. Реализовать наследование классов и понять принципы его реализования на Python"""

"""5.1. Создадим один класс, который отвечает за расчет данных, а второй за построение графика. Применим принцип наследования и реализуем задачу из пункта 4."""



class OnlyPlotClass:

    def plotGraph(self, data):
        self.data = data
        plt.plot(self.data[1], self.data[0], '--')
        plt.show()



class OnlyMathFun(OnlyPlotClass):
    """The class is built to plot mathematic functions"""

    def __init__(self, f1, U):
        """Here you define some attributes of the class as default"""
        #super().__init__(self)
        self.f1 = f1
        self.u_max = U

    def calculate(self, time):
        u = self.u_max * ma.cos(2 * ma.pi * self.f1 * time)
        return u

    def set_data(self, dotes, pdotes=20):
        self.data = ([self.calculate(t / (self.f1 * pdotes)) for t in range(dotes)],
                     [t / (self.f1 * pdotes) for t in range(dotes)])

    def plot(self):
        super().plotGraph(self.data)


class1 = OnlyPlotClass()
class2 = OnlyMathFun(50, 220)
class2.set_data(100)
class2.plot()