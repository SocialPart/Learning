##calcs

import numpy as np
import sympy as sym
from sympy import Poly
from sympy import Matrix, solve_linear_system
import matplotlib.pyplot as plt

"""Выполнить прогнозирование активной нагрузки на Т5 момент времени. 
Поиск прогнозного значения осуществить с использованием полиномов первой и второй степени. Выбрать лучшую модель."""

"""Начальные данные"""

data = {'t1': 700, 't2': 720, 't3': 730, 't4': 720}
keys = list(data.keys())
items = list(data.values())
print(items)

#Создадим переменную alpha и beta как alpha и beta с помощью функции sym.Symbol().

alpha_lin = sym.symbols('alpha_lin')
beta_lin = sym.symbols('beta_lin')
alpha_kv = sym.symbols('alpha_kv')
beta_kv = sym.symbols('beta_kv')
gamma_kv = sym.symbols('gamma_kv')
t = sym.symbols('t')

"Составление полинома первого порядка по методу наименьших квадратов"

S_lin = (1/4) * (((alpha_lin + beta_lin * 1 - data['t1']) ** 2) +
                 ((alpha_lin + beta_lin * 2 - data['t2']) ** 2) +
                 ((alpha_lin + beta_lin * 3 - data['t3']) ** 2) +
                 ((alpha_lin + beta_lin * 4 - data['t4']) ** 2))

"Взятие частной производной по alpha"
S_lin_diff_a = Poly(sym.diff(S_lin, alpha_lin))
print('Частная производная по alpha', S_lin_diff_a)
"Взятие коэффициентов в виде списка [x*alpha, y*beta, z] -> [x,y,z]"
lin_coefs_da = Poly(S_lin_diff_a).coeffs()

lin_a_da = lin_coefs_da[0]
lin_b_da = lin_coefs_da[1]
lin_c_da = lin_coefs_da[2]
"Взятие частной производной по beta"
S_lin_diff_b = Poly(sym.diff(S_lin, beta_lin))
print('Частная производная по beta', S_lin_diff_b)
"Взятие коэффициентов в виде списка [x*alpha, y*beta, z] -> [x,y,z]"
lin_coefs_db = Poly(S_lin_diff_b).coeffs()

lin_a_db = lin_coefs_db[0]
lin_b_db = lin_coefs_db[1]
lin_c_db = lin_coefs_db[2]

"Составление матрицы где частные производные приравниваем к нулю,переносим свободные члены в правую часть"
system_lin = Matrix(((lin_a_da, lin_b_da, -1 * lin_c_da), (lin_a_db, lin_b_db, -1 * lin_c_db)))
"""Решение системы"""
lin_solve = solve_linear_system(system_lin, alpha_lin, beta_lin)
"Результирующие коэффициенты"
res_lin_alpha = lin_solve.get(alpha_lin)
res_lin_beta = lin_solve.get(beta_lin)

"""Составление полинома"""
lin_poly = Poly(res_lin_alpha + res_lin_beta * t)
print("Полином первого порядка имеет вид:", lin_poly)

"""Составление полинома второй степени по методу наименьших квадратов"""

S_kv = (1/4) * (((alpha_kv + beta_kv * 1 + gamma_kv * (1**2) - data['t1']) ** 2) +
                ((alpha_kv + beta_kv * 2 + gamma_kv * (2**2) - data['t2']) ** 2) +
                ((alpha_kv + beta_kv * 3 + gamma_kv * (3**2) - data['t3']) ** 2) +
                ((alpha_kv + beta_kv * 4 + gamma_kv * (4**2) - data['t4']) ** 2))

"Взятие частной производной по alpha"
S_kv_diff_a = Poly(sym.diff(S_kv, alpha_kv))
print('ЧП по alpha',S_kv_diff_a)
"Взятие коэффициентов в виде списка [x*alpha, y*beta, z] -> [x,y,z]"
kv_coefs_da = Poly(S_kv_diff_a).coeffs()
kv_a_da, kv_b_da, kv_g_da, kv_c_da = kv_coefs_da[0], kv_coefs_da[1], kv_coefs_da[2], kv_coefs_da[3]

"Взятие частной производной по beta"
S_kv_diff_b = Poly(sym.diff(S_kv, beta_kv))
print('ЧП по beta',S_kv_diff_b)
"Взятие коэффициентов в виде списка [x*alpha, y*beta, z] -> [x,y,z]"
kv_coefs_db = Poly(S_kv_diff_b).coeffs()
kv_a_db, kv_b_db, kv_g_db, kv_c_db = kv_coefs_db[0], kv_coefs_db[1], kv_coefs_db[2], kv_coefs_db[3]

"Взятие частной производной по gamma"
S_kv_diff_g = Poly(sym.diff(S_kv, gamma_kv))
print('ЧП по gamma',S_kv_diff_g)
"Взятие коэффициентов в виде списка [x*alpha, y*beta, z] -> [x,y,z]"
kv_coefs_dg = Poly(S_kv_diff_g).coeffs()
kv_a_dg, kv_b_dg, kv_g_dg, kv_c_dg = kv_coefs_dg[0], kv_coefs_dg[1], kv_coefs_dg[2], kv_coefs_dg[3]

"Составление матрицы где частные производные приравниваем к нулю,переносим свободные члены в правую часть"
system_kv = Matrix(((kv_a_da, kv_b_da, kv_g_da, -1 * kv_c_da),
                    (kv_a_db, kv_b_db, kv_g_db, -1 * kv_c_db),
                    (kv_a_dg, kv_b_dg, kv_g_dg, -1 * kv_c_dg)))
"""Решение системы"""
lin_solve = solve_linear_system(system_kv, alpha_kv, beta_kv, gamma_kv)
"Результирующие коэффициенты"
res_kv_alpha = lin_solve.get(alpha_kv)
res_kv_beta = lin_solve.get(beta_kv)
res_kv_gamma = lin_solve.get(gamma_kv)

"""Составление полинома"""
kv_poly = Poly(res_kv_alpha + res_kv_beta * t + res_kv_gamma * (t ** 2))
print("Полином второго порядка имеет вид:", kv_poly)

"Выражения для сравнения моделей посредством метода наименьших квадратов"
lin = lin_poly.as_expr()
kv = kv_poly.as_expr()


res_lin = 0
res_kv = 0
"""Расчёт погрешностей" составление списков для графика"""

list_lin = []
list_kv = []
for i in range(1, 5):
    res_lin += (lin_poly.as_expr({t:i}) - data.get(keys[i-1]))**2
    list_lin.append(lin_poly.as_expr({t: i}))
res_lin = res_lin / 4
for i in range(1, 5):
    res_kv += (kv_poly.as_expr({t:i}) - data.get(keys[i-1]))**2
    list_kv.append(kv_poly.as_expr({t: i}))
res_kv = res_kv / 4
print(res_lin, res_kv, '\n', list_lin, list_kv)

print(kv_poly.as_expr({t: 5}))
# print(0,25 * sym.Sum(lin_poly - data.get(keys[n]), n, 1, 4))
#print(sym.solve(lin_poly))

str = keys.copy()
print(keys)
str.append('t5')
list_lin.append(lin_poly.as_expr({t:5}))
print(list_lin)
list_kv.append(kv_poly.as_expr({t:5}))
print()
fig, ax = plt.subplots(figsize=[10, 7])

ax.plot(str, list_lin, label='Полином первой степени \n {0}+{1}*t'.format(res_lin_alpha.evalf(4), res_lin_beta.evalf(4)), color='green', linewidth=2, markersize=5)

ax.plot(str, list_kv, label='Полином второй степени \n {0}+{1}*t+{2}*t^2'.format(res_kv_alpha.evalf(4), res_kv_beta.evalf(4), res_kv_gamma.evalf(4)), color='red', linewidth=2, markersize=5)

ax.set_title('Прогноз активной нагрузки ', fontsize=20, verticalalignment='bottom', fontstyle='italic')
ax.set_facecolor('#EEEEEE')
ax.legend(loc="upper left", fontsize=9).get_frame().set_color('gray')

ax.grid(color='grey', linestyle='--', linewidth=1)
ax.set_xlabel('Моменты времени', fontsize=14)

ax.set_ylabel('Мощность', fontsize=14)
plt.plot(keys, items, label='График потребления', color='blue', marker='x', linewidth=2, markersize=5)
ax.legend(loc="upper left", fontsize=9).get_frame().set_color('gray')


plt.show()