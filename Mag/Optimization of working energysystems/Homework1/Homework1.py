import numpy as np
import sympy as sym
from docxtpl import DocxTemplate
import docal

"""Начальные данные"""

data = {'t1': "700", 't2': "730", 't3': "730", 't4': "720"}

doc = DocxTemplate("Mag/Optimization of working energysystems/Homework1/Шаблон для заполнения.docx")
doc.render(data)
doc.save("Mag/Optimization of working energysystems/Homework1/Ефимов А.С. 4 вариант.docx")