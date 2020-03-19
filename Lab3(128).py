"""
1. Скласти матрицю планування для дробового трьохфакторного експерименту. Провести
експеримент в усіх точках факторного простору, повторивши N експериментів, де N – кількість
експериментів (рядків матриці планування) в усіх точках факторного простору – знайти значення
функції відгуку У. Значення функції відгуку знайти у відповідності з варіантом діапазону,
зазначеного далі (випадковим чином).

2. Знайти коефіцієнти лінійного рівняння регресії. Записати лінійне рівняння регресії.

3. Провести 3 статистичні перевірки.
"""
"""
x1min = -15
x1max = 30
x2min = 30
x2max = 80
x3min = 30
x3max = 35

"""

import random
import numpy as np
import math


def wrapper(func):
    def inner_func(*args, **kwargs):
        print(f"{'':-^49}\nВиконаємо перевірку")
        func(*args)
        print(f"{'':-^49}")
    return inner_func

x1min = -15
x1max = x2min = x3min = 30
x2max = 80
x3max = 35

x1_cod = [-1, -1, 1, 1]
x2_cod = [-1, 1, -1, 1]
x3_cod = [-1, 1, 1, -1]

ymin = 200 + round((x1max + x2max + x3max) / 3)
ymax = 200 + round((x1min + x2min + x3min) / 3)

X1 = [x1min, x1min, x1max, x1max]
X2 = [x2min, x2max, x2min, x2max]
X3 = [x3min, x3max, x3max, x3min]
X_ALL = [X1, X2, X3]
Y1 = [random.randint(ymax, ymin) for _ in range(4)]
Y2 = [random.randint(ymax, ymin) for _ in range(4)]
Y3 = [random.randint(ymax, ymin) for _ in range(4)]

# Кодовані значення
print("Кодовані значення Х")
print("|{0: ^3}|{1: ^3}|{2: ^3}|\n".format("X1", "X2", "X3") +
      "{:-^13}\n".format("") +
      "|{0: ^3}|{1: ^3}|{2: ^3}|\n".format(x1_cod[0], x2_cod[0], x3_cod[0]) +
      "{:-^13}\n".format("") +
      "|{0: ^3}|{1: ^3}|{2: ^3}|\n".format(x1_cod[1], x2_cod[1], x3_cod[1]) +
      "{:-^13}\n".format("") +
      "|{0: ^3}|{1: ^3}|{2: ^3}|\n".format(x1_cod[2], x2_cod[2], x3_cod[2]) +
      "{:-^13}\n".format("") +
      "|{0: ^3}|{1: ^3}|{2: ^3}|\n".format(x1_cod[3], x2_cod[3], x3_cod[3]) +
      "{:-^13}\n".format(""))

# Натуральні значення

print("Натуральні значення з m=3")
print("|{0: ^3}|{1: ^3}|{2: ^3}|{3: ^3}|{4: ^3}|{5: ^3}|\n".format("X1", "X2", "X3", "Y1", "Y2", "Y3") +
      "{:-^25}".format(""))
for i in range(4):
    print(
        "|{0: ^3}|{1: ^3}|{2: ^3}|{3: ^3}|{4: ^3}|{5: ^3}|\n".format(X1[i], X2[i], X3[i], Y1[i], Y2[i], Y3[i]) +
        "{:-^25}".format(""))

# Знайдемо середні значення функції відгуку за рядками
y1av = (Y1[0]+Y2[0]+Y3[0])/3
y2av = (Y1[1]+Y2[1]+Y3[1])/3
y3av = (Y1[2]+Y2[2]+Y3[2])/3
y4av = (Y1[3]+Y2[3]+Y3[3])/3
y_averages = [y1av, y2av, y3av, y4av]

mx1 = sum(X1)/4
mx2 = sum(X2)/4
mx3 = sum(X3)/4

my = (y1av + y2av + y3av + y4av)/4

a1 = (X1[0]*y1av + X1[1]*y2av + X1[2]*y3av + X1[3]*y4av)/4
a2 = (X2[0]*y1av + X2[1]*y2av + X2[2]*y3av + X2[3]*y4av)/4
a3 = (X3[0]*y1av + X3[1]*y2av + X3[2]*y3av + X3[3]*y4av)/4

a11 = (X1[0]*X1[0] + X1[1]*X1[1] + X1[2]*X1[2] + X1[3]*X1[3])/4
a22 = (X2[0]*X2[0] + X2[1]*X2[1] + X2[2]*X2[2] + X2[3]*X2[3])/4
a33 = (X3[0]*X3[0] + X3[1]*X3[1] + X3[2]*X3[2] + X3[3]*X3[3])/4
a12 = a21 = (X1[0]*X2[0] + X1[1]*X2[1] + X1[2]*X2[2] + X1[3]*X2[3])/4
a13 = a31 = (X1[0]*X3[0] + X1[1]*X3[1] + X1[2]*X3[2] + X1[3]*X3[3])/4
a23 = a32 = (X2[0]*X3[0] + X2[1]*X3[1] + X2[2]*X3[2] + X2[3]*X3[3])/4


left = np.array([[1, mx1, mx2, mx3],
                 [mx1, a11, a12, a13],
                 [mx2, a12, a22, a23],
                 [mx3, a13, a23, a33]])

right = np.array([my, a1, a2, a3])
b = np.linalg.solve(left, right)

print("Отримане рівняння регресії")
print(f"y = {b[0]:.2f} + {b[1]:.2f}*x1 + {b[2]:.2f}*x2 + {b[3]:.2f}*x3")

@wrapper
def check(allX, coef, y_av):
    for i in range(len(allX[0])):
        print(f"{coef[0]:.2f} + {coef[1]:.2f}*{allX[0][i]} + {coef[2]:.2f}*{allX[1][i]} + {coef[3]:.2f}*{allX[2][i]} = ", end=" ")
        print(coef[0]+coef[1]*allX[0][i]+coef[2]*allX[1][i]+coef[3]*allX[2][i])
    print(y_av)


check(X_ALL, b, y_averages)


# Використання матриці з нормованими значеннями факторів
# Знайдемо значення дисперсії по рядках

d1 = ((Y1[0] - y1av)**2 + (Y2[0] - y2av)**2 + (Y3[0] - y3av)**2) / 3
d2 = ((Y1[1] - y1av)**2 + (Y2[1] - y2av)**2 + (Y3[1] - y3av)**2) / 3
d3 = ((Y1[2] - y1av)**2 + (Y2[2] - y2av)**2 + (Y3[2] - y3av)**2) / 3
d4 = ((Y1[3] - y1av)**2 + (Y2[3] - y2av)**2 + (Y3[3] - y3av)**2) / 3

all_S = [d1, d2, d3, d4]
Gp = max(all_S) / sum(all_S)

m = 3
f1 = m - 1
f2 = N = 4
# Рівень значимості 0.95
# Gt = 0.7679
if Gp < 0.7679:
    print("Дисперсія однорідна")
else:
    print("Дисперсія неоднорідна")

# Оцінимо значимість коефіцієнтів регресії згідно критерію Стюдента

Sb = sum(all_S) / N
SSb = Sb / (N * m)

notSsb = math.sqrt(SSb)

beta0 = (y1av*1 + y2av*1 + y3av*1 + y4av*1)/4
beta1 = (y1av*(-1) + y2av*(-1) + y3av*1 + y4av*1)/4
beta2 = (y1av*(-1) + y2av*1 + y3av*(-1) + y4av*1)/4
beta3 = (y1av*(-1) + y2av*1 + y3av*1 + y4av*(-1))/4

t0 = abs(beta0)/notSsb
t1 = abs(beta1)/notSsb
t2 = abs(beta2)/notSsb
t3 = abs(beta3)/notSsb
all_T = [t0, t1, t2, t3]
f3 = f1 * f2 # 8, отже, значення Tтабл = 2.306

for i in range(4):
    if all_T[i] < 2.306:
        print(f"Приймаємо b{i} при рівні значимості 0.05 незначні. Виключаємо його з рівняння")
        b[i] = 0

print(f"y = {b[0]} + {b[1]}*x1 + {b[2]}*x2 + {b[3]}*x3")

yy1 = b[0] + b[1]*X1[0] + b[2]*X2[0] + b[3]*X3[0]
yy2 = b[0] + b[1]*X1[1] + b[2]*X2[1] + b[3]*X3[1]
yy3 = b[0] + b[1]*X1[2] + b[2]*X2[2] + b[3]*X3[2]
yy4 = b[0] + b[1]*X1[3] + b[2]*X2[3] + b[3]*X3[3]

# Критерій Фішера
d = 2
f4 = N - d
Sad = ((yy1 - y1av)**2 + (yy2 - y2av)**2 + (yy3 - y3av)**2 + (yy4 - y4av)**2)*(m/(N-d))
Fp = Sad/Sb
# Ft берем із таблиці 8 рядяк 2 стовпець Ft = 4.5
Ft = 4.5
if Fp > Ft:
    print("Fp=", round(Fp, 2), ">Ft", Ft, "Рівняння неадекватно оригіналу")
else:
    print("Fp=", round(Fp, 2), "<Ft", Ft, "Рівняння адекватно оригіналу")
