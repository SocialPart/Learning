##foo.py

from docxtpl import DocxTemplate
import docal
from calcs import *

"""Начальные данные"""

data = {'t1': "700", 't2': "730", 't3': "730", 't4': "720"}

doc = DocxTemplate("Шаблон для заполнения.docx")
doc.render(data)
doc.save("Ефимов А С 4 вариант.docx")


